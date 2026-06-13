# Clear Coding Comments & Docstrings (ការសរសេរ Comment និងឯកសារកូដ)

ការសរសេរ Comment ឬ Docstring ក្នុងកូដជាភាសាអង់គ្លេសប្រកបដោយភាពច្បាស់លាស់ ជួយឱ្យអ្នកសរសេរកូដផ្សេងទៀតអាចយល់ពីកូដរបស់អ្នកបានលឿន និងកាត់បន្ថយពេលវេលាថែទាំប្រព័ន្ធ។

Writing clear English comments and docstrings in your code helps other developers understand your logic quickly, improving maintainability and reducing friction in team collaboration.

---

## 💡 ១. គោលការណ៍សំខាន់ៗនៃការសរសេរ Comment (Core Principles)

* **ពន្យល់ពី "ហេតុអ្វី" មិនមែន "អ្វី" (Explain WHY, not WHAT):** កុំសរសេរ Comment ដែលគ្រាន់តែនិយាយឡើងវិញពីអ្វីដែលកូដធ្វើ។
  - *មិនល្អ (Bad):*
    ```java
    // Increment i by 1
    i++;
    ```
  - *ល្អ (Good - ពន្យល់ពីគោលបំណង):*
    ```java
    // Move to the next page in the pagination sequence
    i++;
    ```
* **ខ្លីខ្លឹម និងចំចំណុច (Be concise and precise):** ប្រើពាក្យឱ្យបានតិច ប៉ុន្តែមានន័យគ្រប់គ្រាន់។

---

## ⚙️ ២. របៀបសរសេរ Docstring តាមស្តង់ដារ (Standard Docstring Formatting)

Docstring ត្រូវប្រើដើម្បីពណ៌នាពីមុខងារ ថ្នាក់ ឬកញ្ចប់កូដ។ ភាសាអង់គ្លេសដែលប្រើក្នុង Docstring ច្រើនតែចាប់ផ្តើមដោយ **Imperative Mood** (កិរិយាសព្ទបញ្ជា/ចង្អុលបង្ហាញ) ដូចជា `Calculate`, `Return`, `Verify` (មិនមែន *Calculates*, *Returns*, *Verifies* ឡើយ)។

### ឧទាហរណ៍ក្នុង Java (JavaDoc):
```java
/**
 * Calculate the total price of products in the shopping cart,
 * including applicable VAT and discount rates.
 *
 * @param cart the list of items in the cart
 * @param discount the percentage of discount to apply (0.0 to 1.0)
 * @return the final calculated price as double
 * @throws IllegalArgumentException if the discount is out of range
 */
public double calculateTotal(List<Item> cart, double discount) {
    // ... logic ...
}
```

---

## 🛠️ ឃ្លាទូទៅសម្រាប់ Comment (Common Comment Phrases)

* **TODO:** អ្វីដែលត្រូវធ្វើបន្ថែមនៅពេលក្រោយ។
  - `// TODO: Refactor this class to use a thread-safe cache.`
* **FIXME:** បញ្ហាក្នុងកូដដែលត្រូវកែតម្រូវជាបន្ទាន់។
  - `// FIXME: Handle NullPointerException when database returns empty query results.`
* **NOTE:** ការបញ្ជាក់បន្ថែមអំពីចំណុចពិសេស ឬករណីពិសេសក្នុងកូដ។
  - `// NOTE: We use BCrypt here to comply with global security compliance.`

---
🔗 **[ត្រឡប់ទៅមេរៀនមុន (Back to Module Index)](../README.md)**
