# Test Examples

Real output from Commit Critic testing various repositories.

## Tests

| Test | Repository | Method | File |
|------|------------|--------|------|
| Local Analysis | commit-critic (this repo) | CLI | [local-repo-analysis.md](local-repo-analysis.md) |
| Remote URL Analysis | anthropics/anthropic-cookbook | CLI/API | [remote-url-analysis.md](remote-url-analysis.md) |

## Running Tests

### CLI (No server needed)

```bash
# Test local repository
make analyze

# Test remote URL
make analyze-url

# Run quick tests
make test
```

### LangGraph API (Server required)

```bash
# Start server
make up

# Create thread
curl -X POST http://localhost:2024/threads -H "Content-Type: application/json" -d '{}'

# Run analysis (replace THREAD_ID)
curl -X POST "http://localhost:2024/threads/THREAD_ID/runs" \
  -H "Content-Type: application/json" \
  -d '{"assistant_id":"commit_critic","input":{"messages":[{"role":"user","content":"Analyze last 10 commits"}]}}'
```

## Scoring Criteria

Commits are scored 1-10 based on:

| Criterion | Points | Description |
|-----------|--------|-------------|
| Clarity   | 0-3    | Does it explain WHAT changed? |
| Context   | 0-3    | Does it explain WHY? |
| Format    | 0-2    | Follows conventional commits? |
| Scope     | 0-2    | Is the affected area clear? |

**Categories:**
- **needs_work (1-3)**: Vague, one-word, or unclear
- **acceptable (4-6)**: Understandable but could be better
- **excellent (7-10)**: Clear, scoped, and contextual
