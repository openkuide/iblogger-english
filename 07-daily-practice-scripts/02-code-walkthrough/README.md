# Peer Review & Code Walkthroughs (ស្គ្រីបពន្យល់កូដ និងការ Review)

ខាងក្រោមនេះជាស្គ្រីបសម្រាប់ពន្យល់កូដរបស់អ្នកកំឡុងពេល Review ជាមួយសមាជិកក្រុម ឬ Senior Developer។

Below are the speaking scripts for code walkthroughs, split into Professional and Natural/Casual styles.

---

## 🗣️ ស្គ្រីបទី ១៖ ការណែនាំអំពីកូដថ្មី (Introducing your PR)

### 💼 Professional Version
> "Hi team, I’ve created this Pull Request to address the memory leak issue in the connection pooling. The main goal is to ensure database connections are properly closed after each transaction."

### 🔥 Natural/Casual Version (Slay!)
> "Hey guys, I **opened this PR** to **fix the memory leak** we've been having with the connection pool. The **whole point of this** is to make sure we're **cleaning up connections** after each transaction."

* **Key Vocabulary:**
  - *opened a PR:* បង្កើត Pull Request (instead of *created*)
  - *whole point of this:* គោលបំណងចម្បងនៃកូដនេះ (instead of *main goal*)
  - *cleaning up:* បោសសម្អាត/បិទចោល (instead of *properly closed*)

---

## 🗣️ ស្គ្រីបទី ២៖ ការនាំដើរមើលកូដតាមបន្ទាត់ (Walking through specific files)

### 💼 Professional Version
> "If we look at DatabaseConnection.java, line 45, you will see that I've replaced the manual connection close block to prevent the NullPointerException we saw in the logs."

### 🔥 Natural/Casual Version (Slay!)
> "If we **hop over** to DatabaseConnection.java, line 45, **you can see** I **ditched the manual close block**. This should **kill the NullPointerException** that showed up in the logs."

* **Key Vocabulary:**
  - *hop over to:* ផ្លាស់ទីភ្នែកទៅមើល (instead of *look at*)
  - *ditched:* បោះបង់ចោល/ជំនួស (instead of *replaced/removed*)
  - *kill:* កម្ចាត់/ដោះស្រាយ (instead of *prevent/resolve*)

---

## 🗣️ ស្គ្រីបទី ៣៖ ការសុំយោបល់កែលម្អ (Asking for feedback)

### 💼 Professional Version
> "I am confident with this implementation, but I wanted to get your opinion on the configuration setup on line 120. Please let me know if you see any room for optimization."

### 🔥 Natural/Casual Version (Slay!)
> "I'm **pretty good with how this looks**, but I’d love to **get your eyes on** the config setup on line 120. **Let me know if I missed anything** or if we can make it cleaner."

* **Key Vocabulary:**
  - *pretty good with...:* មានទំនុកចិត្តលើ (instead of *confident with*)
  - *get your eyes on:* សុំអ្នកជួយមើល (instead of *get your opinion/look at*)
  - *make it cleaner:* ធ្វើឱ្យកូដមានរបៀប/ប្រសើរជាងមុន (instead of *optimize*)

---
🔗 **[ត្រឡប់ទៅមេរៀនមុន (Back to Module Index)](../README.md)**
