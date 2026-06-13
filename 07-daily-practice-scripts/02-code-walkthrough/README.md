# Peer Review & Code Walkthroughs (ស្គ្រីបពន្យល់កូដ និងការ Review)

ជំពូកនេះជួយអ្នកក្នុងការនាំសមាជិកក្រុម ឬ Senior Developer មើលកូដរបស់អ្នកកំឡុងពេល Review។

Practice walk-through scripts for code reviews, including spoken linking guides and Khmer translations.

---

## 🗣️ ស្គ្រីបទី ១៖ ការណែនាំអំពីកូដថ្មី (Introducing your PR)

### 💼 Professional Version
> "Hi team, I’ve created this Pull Request to address the memory leak issue in the connection pooling. The main goal is to ensure database connections are properly closed after each transaction."

### 🔥 Natural/Casual Version (Slay!)
> "Hey guys, I **opened this PR** to **fix the memory leak** we've been having with the connection pool. The **whole point of this** is to make sure we're **cleaning up connections** after each transaction."

* **🗣️ Spoken & Linking Guide (គន្លឹះភ្ជាប់សំឡេង):**
  - **opened this** -> និយាយភ្ជាប់គ្នាថា **"ope-ndis"** (/əʊ.pənd-ðɪs/)
  - **point of** -> និយាយភ្ជាប់គ្នាថា **"poin-tov"** (/pɔɪnt-ɒv/)
  - **cleaning up** -> និយាយភ្ជាប់គ្នាថា **"clea-ning-up"**
* **💬 អត្ថន័យជាភាសាខ្មែរ (Khmer Meaning):**
  - *«សួស្តីអ្នកទាំងអស់គ្នា ខ្ញុំបានបង្កើត PR នេះ ដើម្បីជួសជុល memory leak ដែលយើងធ្លាប់ជួបប្រទះជាមួយ connection pool។ គោលបំណងចម្បងនៃកូដនេះគឺដើម្បីធានាថាយើងបិទ/បោសសម្អាតរាល់ការតភ្ជាប់ (connections) ក្រោយពេលដំណើរការ transaction នីមួយៗរួចរាល់។»*

---

## 🗣️ ស្គ្រីបទី ២៖ ការនាំដើរមើលកូដតាមបន្ទាត់ (Walking through specific files)

### 💼 Professional Version
> "If we look at DatabaseConnection.java, line 45, you will see that I've replaced the manual connection close block to prevent the NullPointerException we saw in the logs."

### 🔥 Natural/Casual Version (Slay!)
> "If we **hop over** to DatabaseConnection.java, line 45, **you can see** I **ditched the manual close block**. This should **kill the NullPointerException** that showed up in the logs."

* **🗣️ Spoken & Linking Guide (គន្លឹះភ្ជាប់សំឡេង):**
  - **hop over** -> និយាយភ្ជាប់គ្នាថា **"ho-pover"** (/hɒp-əʊ.və/)
  - **showed up** -> និយាយភ្ជាប់គ្នាថា **"show-dup"** (/ʃəʊd-ʌp/)
  - **in the** -> និយាយលឿនៗថា **"in-th'"**
* **💬 អត្ថន័យជាភាសាខ្មែរ (Khmer Meaning):**
  - *«ប្រសិនបើយើងលោតទៅមើល DatabaseConnection.java បន្ទាត់ទី ៤៥ អ្នកនឹងឃើញថាខ្ញុំបានដក manual close block ចេញ។ របៀបនេះនឹងកម្ចាត់ចោលនូវ NullPointerException ដែលធ្លាប់បង្ហាញនៅក្នុង log files នោះ។»*

---

## 🗣️ ស្គ្រីបទី ៣៖ ការសុំយោបល់កែលម្អ (Asking for feedback)

### 💼 Professional Version
> "I am confident with this implementation, but I wanted to get your opinion on the configuration setup on line 120. Please let me know if you see any room for optimization."

### 🔥 Natural/Casual Version (Slay!)
> "I'm **pretty good with how this looks**, but I’d love to **get your eyes on** the config setup on line 120. **Let me know if I missed anything** or if we can make it cleaner."

* **🗣️ Spoken & Linking Guide (គន្លឹះភ្ជាប់សំឡេង):**
  - **get your** -> និយាយភ្ជាប់គ្នាថា **"ge-chur"** (/ɡet-jɔː/)
  - **eyes on** -> និយាយភ្ជាប់គ្នាថា **"eye-zon"** (/aɪz-ɒn/)
  - **missed anything** -> និយាយភ្ជាប់គ្នាថា **"miss-dany-thing"** (/mɪst-eni.θɪŋ/)
* **💬 អត្ថន័យជាភាសាខ្មែរ (Khmer Meaning):**
  - *«ខ្ញុំគិតថាកូដនេះរៀបចំបានល្អហើយ ប៉ុន្តែខ្ញុំចង់សុំឱ្យអ្នកជួយពិនិត្យមើលការកំណត់រចនាសម្ព័ន្ធនៅបន្ទាត់ទី ១២០ បន្តិច។ ប្រាប់ខ្ញុំផង ប្រសិនបើខ្ញុំភ្លេចចំណុចណាមួយ ឬប្រសិនបើយើងអាចរៀបចំវាឱ្យកាន់តែស្អាតជាងនេះ។»*

---
🔗 **[ត្រឡប់ទៅមេរៀនមុន (Back to Module Index)](../README.md)**
