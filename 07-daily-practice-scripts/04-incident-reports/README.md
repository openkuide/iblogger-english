# Handling Incident Reports (ស្គ្រីបរាយការណ៍បញ្ហាបន្ទាន់)

នៅពេលប្រព័ន្ធផលិតកម្ម (Production Server) ជួបប្រទះបញ្ហាគាំង ឬមាន bug ធ្ងន់ធ្ងរ ការទំនាក់ទំនងជាភាសាអង់គ្លេសឱ្យបានច្បាស់លាស់ និងទាន់ពេលវេលាគឺសំខាន់បំផុត ដើម្បីរក្សាភាពស្ងប់ស្ងាត់ និងរួមគ្នាដោះស្រាយ។

During system outages or critical bugs on production, clear and timely communication is essential. Memorize these scripts to announce issues and report updates calm and structured.

---

## 🗣️ ស្គ្រីបទី ១៖ ការរាយការណ៍បញ្ហាដំបូងបង្អស់ (Reporting the incident)

> "Hi everyone, we have a critical incident on production. The **[payment service]** is currently unresponsive, resulting in 502 Bad Gateway errors for checkout requests. I am investigating the logs right now to identify the root cause. I will keep you updated as soon as I have more information."

### 🗣️ អានជាសំឡេងខ្មែរសម្រួល (Khmer Translation)
> «សួស្តីអ្នកទាំងអស់គ្នា យើងមានបញ្ហាបន្ទាន់នៅលើ production។ **[payment service]** បច្ចុប្បន្នមិនឆ្លើយតបឡើយ ដែលបណ្តាលឱ្យមានកំហុស 502 Bad Gateway សម្រាប់ការទូទាត់ប្រាក់។ ខ្ញុំកំពុងស៊ើបអង្កេតលើ logs នៅពេលនេះ ដើម្បីស្វែងរកមូលហេតុចម្បង។ ខ្ញុំនឹងជូនដំណឹងជាបន្តបន្ទាប់នៅពេលទទួលបានព័ត៌មានបន្ថែម។»

---

## 🗣️ ស្គ្រីបទី ២៖ ការរាយការណ៍វឌ្ឍនភាពនៃការដោះស្រាយ (Providing updates)

> "An update on the production issue: We identified that the database connection pool was full due to a sudden surge in traffic. To mitigate this, we have increased the pool limit on Kubernetes and restarted the service. The checkout system is back online, and we are monitoring the resource usage closely."

### 🗣️ អានជាសំឡេងខ្មែរសម្រួល (Khmer Translation)
> «បច្ចុប្បន្នភាពលើបញ្ហា production៖ យើងបានរកឃើញថា database connection pool ពេញ ដោយសារការកើនឡើងភ្លាមៗនៃចរាចរណ៍អ្នកប្រើប្រាស់ (traffic)។ ដើម្បីដោះស្រាយបញ្ហានេះ យើងបានបង្កើនដែនកំណត់ pool លើ Kubernetes និងចាប់ផ្តើម service ឡើងវិញ។ ប្រព័ន្ធ checkout ដំណើរការឡើងវិញហើយ ហើយយើងកំពុងតាមដានការប្រើប្រាស់ធនធានយ៉ាងយកចិត្តទុកដាក់។»

---

## 🗣️ ស្គ្រីបទី ៣៖ របាយការណ៍ក្រោយការដោះស្រាយ (Post-Incident summary)

> "The issue has been completely resolved. The root cause was an unindexed query in the **[orders table]**, which caused slow transactions. I have added the missing database indexes and verified that the transaction latency is back to normal. I will write a post-mortem report by this afternoon."

### 🗣️ អានជាសំឡេងខ្មែរសម្រួល (Khmer Translation)
> «បញ្ហាត្រូវបានដោះស្រាយទាំងស្រុងហើយ។ មូលហេតុចម្បងគឺ query ដែលគ្មាន index នៅក្នុង **[orders table]** ដែលបណ្តាលឱ្យ transaction យឺត។ ខ្ញុំបានបន្ថែម index លើ database រួចហើយ និងបានផ្ទៀងផ្ទាត់ថា latency របស់ transaction បានត្រឡប់មកធម្មតាវិញហើយ។ ខ្ញុំនឹងសរសេររបាយការណ៍សង្ខេបក្រោយបញ្ហា (post-mortem report) ឱ្យបានរួចរាល់នៅរសៀលនេះ។»

---
🔗 **[ត្រឡប់ទៅមេរៀនមុន (Back to Module Index)](../README.md)**
