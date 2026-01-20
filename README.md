# Commit Critic

AI-powered commit message analyzer using LangGraph Deep Agents.

## Overview

Commit Critic is a terminal tool that helps developers write better commit messages. It uses Claude (Anthropic) to:

1. **Analyze Mode**: Review commit history and score message quality (1-10)
2. **Write Mode**: Generate well-formatted commits based on staged changes

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Rajathbharadwaj/commit-critic.git
cd commit-critic

# Install dependencies
pip install -r requirements.txt

# Set your Anthropic API key
export ANTHROPIC_API_KEY=sk-ant-...

# Analyze a repository
python commit_critic.py --analyze --url="https://github.com/steel-dev/steel-browser"
```

## Architecture

Built using LangGraph's `deepagents` library with a multi-agent architecture:

```
Main Agent (Orchestrator)
    │
    ├── fetch_commits      → Clone repos & fetch commit history
    ├── analyze_commits    → Score and categorize commit messages
    ├── get_staged_changes → Get git diff --staged
    ├── suggest_commit     → Generate commit messages from diff
    └── execute_commit     → Run git commit
```

**Built-in Context Optimization:**
- `FilesystemMiddleware` - Auto-evicts large tool outputs to files
- `SummarizationMiddleware` - Auto-summarizes when context exceeds limit
- `AnthropicPromptCachingMiddleware` - Caches system prompts for cost reduction

## Usage

### Analyze Commits

```bash
# Analyze last 50 commits from current repository
python commit_critic.py --analyze

# Analyze last 100 commits
python commit_critic.py --analyze --limit 100

# Analyze a remote repository
python commit_critic.py --analyze --url="https://github.com/steel-dev/steel-browser"
```

### Write Commits

```bash
# Stage your changes first
git add .

# Get AI-suggested commit message
python commit_critic.py --write
```

**Interactive Options:**
- `y/yes` - Accept and commit with suggested message
- `r/revise` - Give feedback to revise the suggestion
- `c/custom` - Type your own commit message
- `n/no` - Cancel without committing

## Example Output

Here's a real analysis of the [steel-dev/steel-browser](https://github.com/steel-dev/steel-browser) repository:

<details>
<summary><strong>Click to expand full analysis (50 commits)</strong></summary>

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃             📊 Commit Message Analysis: steel-dev/steel-browser              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

Analysis of the last 50 commits from the repository.

────────────────────────────────────────────────────────────────────────────────

                             📈 Summary Statistics

  Metric                     Value
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Average Score              6.5/10
  Excellent Commits (7-10)   28 (56%)
  Acceptable Commits (4-6)   21 (42%)
  Needs Work (1-3)           1 (2%)

────────────────────────────────────────────────────────────────────────────────

                     🚨 Commits That Need Work (Score 1-3)

                           ❌ 539981d6 - Score: 3/10

 fix: remove arrounious extensionsPath

Issues:
 • Typo: "arrounious" instead of "erroneous"
 • No PR reference
 • Unclear context

Suggested Improvement:
 fix(extensions): remove erroneous extensionsPath configuration

────────────────────────────────────────────────────────────────────────────────

           ⚠️ Acceptable Commits with Room for Improvement (Score 4-6)

                             8610295b - Score: 6/10

 feat: optimise Steel browser performance (#239)

Issue: Missing specific details about what optimizations were made
Suggestion: feat(browser): optimize Steel browser performance with resource
loading improvements

────────────────────────────────────────────────────────────────────────────────

                             c9f49e13 - Score: 5/10

 chore: package bump + conditional mouse paint (#229)

Issue: Combines two unrelated changes (package updates and mouse paint logic)
Suggestion: Should be split into two commits: chore: bump package versions and
feat(ui): add conditional mouse paint

────────────────────────────────────────────────────────────────────────────────

                             f6378a57 - Score: 4/10

 feat: env.DISPLAY (#192)

Issue: Too terse - doesn't explain what this feature does or why
Suggestion: feat(env): add DISPLAY environment variable support for headful
sessions

────────────────────────────────────────────────────────────────────────────────

                      ✅ Well-Written Commits (Score 7-10)

                          🌟 Top Examples (Score 9-10)

                           8ae459a2 - Score: 9/10 ⭐

 fix: wrap GET /sessions response in object to match production API (#213)

Why it's excellent: Perfect explanation with issue reference and detailed body
explaining the problem, root cause (local vs production API mismatch), and
specific changes made.

────────────────────────────────────────────────────────────────────────────────

                           ad079a59 - Score: 9/10 ⭐

 fix: Polyfill `__name` to prevent esbuild errors in Puppeteer context (#184)

Why it's excellent: Clear problem (esbuild errors), solution (polyfill),
specific variable name, and context (Puppeteer). Very well-written and precise.

────────────────────────────────────────────────────────────────────────────────

                           3824d103 - Score: 9/10 ⭐

 feat: Combine UI into API for single application deployment (#186)

Why it's excellent: Clear architectural change with business value (single
deployment) and comprehensive body detailing implementation steps and workflow
updates.

────────────────────────────────────────────────────────────────────────────────

                          🔍 Common Patterns & Issues

                               Recurring Issues:

 1 Vague quantifiers (21% of commits) - "some", "a few", "better" without
   specifics
 2 Multiple unrelated changes (14% of commits) - Should be split into separate
   commits
 3 Wrong commit type (10% of commits) - Using "fix" for docs/chore tasks
 4 Capitalization inconsistencies (8% of commits) - Not following lowercase
   convention
 5 Missing scope (30% of commits) - Not specifying which component was affected

                                   Strengths:

 • ✅ Good use of conventional commits format (98% compliance)
 • ✅ PR references included in nearly all commits
 • ✅ Many commits have detailed bodies explaining context
 • ✅ Clear type categorization (feat/fix/chore/docs)

────────────────────────────────────────────────────────────────────────────────

                               💡 Recommendations

 1 Add scopes - Use format type(scope): subject to clarify which component
   changed
 2 Be specific - Avoid vague words like "some", "better", "improve" without
   context
 3 One concern per commit - Split unrelated changes into separate commits
 4 Lowercase subject - Keep subject line lowercase after the type prefix
 5 Choose correct type - Use chore for build/dependency updates, docs for
   documentation

Overall, the steel-browser repository shows strong commit message discipline
with 98% of commits following conventional format and 56% rated as excellent! 🎉
```

</details>

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

## Conventional Commits Format

The tool encourages the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <subject>

<body>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code restructuring
- `docs`: Documentation
- `test`: Adding tests
- `chore`: Maintenance
- `style`: Formatting
- `perf`: Performance

## Thread Management

Conversations are persisted for continuity:

```bash
# List all conversation threads
python commit_critic.py --threads

# Continue a specific thread
python commit_critic.py --thread <thread_id> --write

# Clear all thread history
python commit_critic.py --clear-threads
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `ANTHROPIC_API_KEY` | Yes | Your Anthropic API key |
| `LANGCHAIN_TRACING_V2` | No | Enable LangSmith tracing |
| `LANGCHAIN_PROJECT` | No | LangSmith project name |

## File Structure

```
commit-critic/
├── commit_critic.py         # Entry point
├── commit_critic/
│   ├── __init__.py          # Package exports
│   ├── cli.py               # CLI interface
│   ├── commit_critic_agent.py # LangGraph deep agent
│   ├── models.py            # Pydantic models
│   ├── prompts.py           # System prompts
│   ├── subagents.py         # 5 atomic subagents
│   └── tools.py             # Git operation tools
├── requirements.txt
├── .env.example
└── README.md
```

## License

MIT
