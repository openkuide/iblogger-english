# Professional Git Commits & PRs (ការសរសេរ Commit Message និង Pull Request)

សារ Commit (Commit Message) និងការពិពណ៌នា Pull Request (PR Description) ដែលច្បាស់លាស់ ជួយឱ្យប្រវត្តិគម្រោង (Project History) មានរបៀបរៀបរយ និងងាយស្រួលរកមើលកន្លែងខុស។

Clear commit messages and Pull Request (PR) descriptions keep the project history clean, logical, and easy to audit for bug regressions.

---

## 📝 ១. ស្តង់ដារនៃការសរសេរ Git Commit Messages (Conventional Commits)

ស្តង់ដារដែលគេនិយមប្រើបំផុតគឺការបែងចែកប្រភេទនៃការផ្លាស់ប្តូរ និងការប្រើ **Imperative Mood** (កិរិយាសព្ទបញ្ជា ដូចជា `Add`, `Fix`, `Update` មិនមែន *Added*, *Fixed*, *Updating* ឡើយ)។

### ទម្រង់ទូទៅ (Structure):
```
<type>(<scope>): <description>
```

### ប្រភេទនៃការផ្លាស់ប្តូរ (Types):
* **feat:** មុខងារថ្មី (feature)។
  - `feat(auth): add JWT-based login mechanism`
* **fix:** ការជួសជុល bug។
  - `fix(db): resolve connection pool starvation during peak traffic`
* **docs:** ការផ្លាស់ប្តូរតែលើឯកសារណែនាំ (documentation)។
  - `docs(readme): update deployment prerequisites and steps`
* **refactor:** ការកែសម្រួលកូដឱ្យស្អាត តែមិនបន្ថែមមុខងារ ឬជួសជុល bug ឡើយ។
  - `refactor(services): simplify user registration validation logic`
* **test:** ការបន្ថែម ឬកែសម្រួល test files។
  - `test(security): add integration tests for session expiration`
* **chore:** ការងារទូទៅដែលមិនពាក់ព័ន្ធនឹងកូដកម្មវិធី (ដូចជា update dependencies)។
  - `chore(deps): upgrade Spring Boot from v3.1 to v3.2`

---

## 📁 ២. គំរូសរសេរ Pull Request (Pull Request Template)

នៅពេលបង្កើត Pull Request ដើម្បីឱ្យមិត្តរួមក្រុម Review កូដ គួរតែសរសេរឱ្យមានរចនាសម្ព័ន្ធត្រឹមត្រូវ៖

### គំរូ PR Description (PR Template):
```markdown
## Description
Provide a brief summary of the changes made and the problem being solved.

## Changes Checklist
- [ ] Added JWT authorization filter.
- [ ] Wrote unit tests for user authentication.
- [ ] Updated API documentation.

## How to Test
Explain how reviewers can run and verify your changes.
1. Run `docker-compose up` to start the database.
2. Launch the backend application on port 8080.
3. Send a POST request to `/api/v1/auth/login` with credentials.
```

---
🔗 **[ត្រឡប់ទៅមេរៀនមុន (Back to Module Index)](../README.md)**
