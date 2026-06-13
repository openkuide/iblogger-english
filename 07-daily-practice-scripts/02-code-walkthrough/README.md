# Peer Review & Code Walkthroughs (ស្គ្រីបពន្យល់កូដ និងការ Review)

នៅពេលអ្នកបង្កើត Pull Request ឬត្រូវធ្វើការ Review កូដជាមួយសមាជិកក្រុម ឬ Senior Developer ការចេះប្រើប្រាស់ឃ្លា និងកថាខណ្ឌខាងក្រោមនឹងជួយឱ្យការបង្ហាញកូដរបស់អ្នកមានភាពច្បាស់លាស់ និងមានលក្ខណៈវិជ្ជាជីវៈ។

During code reviews or pair programming, using these scripts allows you to walk teammates or senior developers through your code changes clearly and professionally.

---

## 🗣️ ស្គ្រីបទី ១៖ ការណែនាំអំពីកូដថ្មី (Introducing your PR)

> "Hi team, I’ve put together this Pull Request to address the **[memory leak issue in the connection pooling]**. The main goal is to ensure that database connections are properly closed after each transaction. I’ve refactored the database utility class to use a try-with-resources statement, which guarantees that connections are closed even if an exception occurs."

### 🗣️ អានជាសំឡេងខ្មែរសម្រួល (Khmer Translation)
> «សួស្តីក្រុមការងារ ខ្ញុំបានរៀបចំ Pull Request នេះឡើង ដើម្បីដោះស្រាយ **[memory leak issue in the connection pooling]**។ គោលបំណងចម្បងគឺធានាថាការតភ្ជាប់មូលដ្ឋានទិន្នន័យត្រូវបានបិទត្រឹមត្រូវបន្ទាប់ពី transaction នីមួយៗ។ ខ្ញុំបាន refactor class ជំនួយមូលដ្ឋានទិន្នន័យឱ្យប្រើប្រាស់ try-with-resources statement ដែលធានាថាការតភ្ជាប់ត្រូវបានបិទ ទោះបីជាមាន exception កើតឡើងក៏ដោយ។»

---

## 🗣️ ស្គ្រីបទី ២៖ ការនាំដើរមើលកូដតាមបន្ទាត់ (Walking through specific files)

> "If we look at **[DatabaseConnection.java]**, line **[45]**, you will see that I've replaced the manual connection close block. Down here on line **[60]**, I also added a check to handle instances where the pool returns a null connection. This prevents the NullPointerException we saw in the logs last week."

### 🗣️ អានជាសំឡេងខ្មែរសម្រួល (Khmer Translation)
> «ប្រសិនបើយើងមើលទៅលើ **[DatabaseConnection.java]** បន្ទាត់ទី **[45]** អ្នកនឹងឃើញថាខ្ញុំបានជំនួស manual connection close block។ នៅខាងក្រោមនេះ បន្ទាត់ទី **[60]** ខ្ញុំក៏បានបន្ថែមការឆែកដើម្បីដោះស្រាយករណីដែល pool ប្រគល់ null connection មកវិញ។ នេះការពារ NullPointerException ដែលយើងបានឃើញនៅក្នុង logs កាលពីសប្តាហ៍មុន។»

---

## 🗣️ ស្គ្រីបទី ៣៖ ការសុំយោបល់កែលម្អ (Asking for feedback / optimization tips)

> "I'm fairly confident with this implementation, but I wanted to get your opinion on the configuration setup on line **[120]**. Do you think the connection timeout limit is too high, or should we keep it as it is? Please let me know if you see any room for optimization."

### 🗣️ អានជាសំឡេងខ្មែរសម្រួល (Khmer Translation)
> «ខ្ញុំមានទំនុកចិត្តគួរសមជាមួយការអនុវត្តនេះ ប៉ុន្តែខ្ញុំចង់សុំយោបល់របស់អ្នកលើការកំណត់រចនាសម្ព័ន្ធនៅបន្ទាត់ទី **[120]**។ តើអ្នកគិតថាដែនកំណត់ connection timeout ខ្ពស់ពេកទេ ឬយើងគួរតែរក្សាវាទុកដដែល? សូមប្រាប់ខ្ញុំផង ប្រសិនបើអ្នកឃើញចំណុចណាដែលអាចធ្វើឱ្យប្រសើរឡើងបាន។»

---
🔗 **[ត្រឡប់ទៅមេរៀនមុន (Back to Module Index)](../README.md)**
