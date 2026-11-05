---
status: observed
source: local workspace / 02 生产代码/shopify-deeplumen-app/README.md, section "连接生产（SSM 端口转发）"
updated: 2026-11-04
scope: project:production-access
confidence: medium
---

# 生产数据库只读连接手册

这份手册记录连接方式和安全边界，不记录数据库密码、AWS access key、SSH key、真实连接串、实例 ID 或秘密参数值。当前只确认本地资料中的连接流程；本次未重新验证生产网络连通性，也没有证明本地资料里的应用连接账号具备只读权限。

## 适用范围

- 仅用于已授权的生产只读核查、证据采集和故障定位。
- 需要 AWS CLI v2、Session Manager Plugin、`psql` 和已获授权的 AWS profile。
- AWS region 目前记录为 `us-east-2`；实际执行前以当前环境的授权配置为准。

## 连接流程

1. 在安全的本地 shell 中确认 AWS 身份，不把身份输出或凭据写入报告。
2. 通过 SSM `AWS-StartPortForwardingSessionToRemoteHost` 启动生产 Postgres 到本地端口的转发。目标实例、远端主机、远端端口和本地端口从受控环境变量或当前运维手册读取，不写进共享仓库。
3. 如需 Redis 诊断，单独建立 Redis 端口转发；不要把 Redis 连接和数据库连接混用。
4. 从 SSM SecureString 或批准的秘密管理器读取数据库密码，只注入当前进程环境；禁止把密码写入脚本、shell history、日志或 Markdown。
5. 将连接指向 `127.0.0.1` 的本地转发端口。生产核查必须使用经批准的只读数据库账号；如果现有资料只提供应用生产 `DATABASE_URL`，不能把它当成只读连接，必须先确认数据库角色和权限。应用生产容器内部的 `DATABASE_URL` 由运行环境注入，不能从代码或共享仓库推断真实值。

示例结构（所有尖括号值必须从受控环境取得）：

```bash
export AWS_REGION="us-east-2"
export AWS_PROFILE="<AUTHORIZED_PROFILE>"

aws sts get-caller-identity --profile "$AWS_PROFILE" --region "$AWS_REGION"

aws ssm start-session \
  --target "$BASTION_INSTANCE" \
  --document-name AWS-StartPortForwardingSessionToRemoteHost \
  --parameters "$PORT_FORWARD_PARAMETERS" \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION"

export PGPASSWORD="$(aws ssm get-parameter \
  --name "$DB_PASSWORD_PARAMETER" \
  --with-decryption \
  --query Parameter.Value \
  --output text \
  --profile "$AWS_PROFILE" \
  --region "$AWS_REGION")"

export DATABASE_URL="postgresql://${DB_USER}@127.0.0.1:${LOCAL_DB_PORT}/${DB_NAME}?sslmode=require"
```

## 只读验证

连接后先执行以下查询，确认目标、账号、事务模式和 schema：

```sql
SELECT current_database(), current_user;
SHOW transaction_read_only;
SHOW search_path;
```

如果账号、数据库或 schema 与预期不符，立即停止，不要继续查询业务表。`transaction_read_only` 的结果和账号权限都不能只凭变量名推断；需要以实际查询结果和数据库权限证据确认。

## 禁止动作

- 不执行 `INSERT`、`UPDATE`、`DELETE`、`TRUNCATE`、`ALTER`、`DROP`、迁移、重置或补数。
- 不在生产数据库运行测试套件；集成测试必须指向隔离测试库。
- 不使用 `aws ssm send-command` 执行未经明确授权的远端命令。
- 不读取管理员密钥、API token 或与当前核查无关的秘密。
- 不因为连接成功、查询返回或字段匹配就宣称业务验收、部署完成或账务确认。

## 证据记录

每次核查记录：

- `observed_at`：观察时间和时区。
- `environment`：生产或测试。
- `access_method`：SSM port forwarding。
- `database`、`user`、`local_port`：可记录非秘密标识；不记录密码和完整连接串。
- `queries`：查询名称和用途，不粘贴敏感结果。
- `result_status`：`observed`、`confirmed`、`blocked` 或 `unverified`。
- `limitations`：未验证的部署、配置、端到端业务或提供方状态。

## 当前限制

本手册来源于本地生产代码仓库的运维说明。本次只整理文档流程，没有重新建立生产隧道，也没有执行生产查询，因此“当前可用”仍为 `unverified`。
