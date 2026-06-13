# Handling Incident Reports (ស្គ្រីបរាយការណ៍បញ្ហាបន្ទាន់)

ជំពូកនេះជួយអ្នកក្នុងការទំនាក់ទំនងកំឡុងពេលប្រព័ន្ធជួបបញ្ហាគាំង ឬមាន bug ធ្ងន់ធ្ងរនៅលើ production។

Incident communication speaking scripts with phonetic linking guides and Khmer translations.

---

## 🗣️ ស្គ្រីបទី ១៖ ការរាយការណ៍បញ្ហាដំបូងបង្អស់ (Reporting the incident)

### 💼 Professional Version
> "Hi everyone, we have a critical incident on production. The payment service is currently unresponsive. I am investigating the logs right now to identify the root cause."

### 🔥 Natural/Casual Version (Slay!)
> "Hey guys, **production is down** right now. The **payment service is completely locked up**, and users are getting 502 errors. I'm **digging into the logs** as we speak to **figure out what's going on**."

* **🗣️ Spoken & Linking Guide (គន្លឹះភ្ជាប់សំឡេង):**
  - **production is** -> និយាយភ្ជាប់គ្នាថា **"pro-duc-tion-iz"** (/prəˈdʌk.ʃən-ɪz/)
  - **locked up** -> និយាយភ្ជាប់គ្នាថា **"lok-tup"** (/lɒkt-ʌp/)
  - **digging into** -> និយាយភ្ជាប់គ្នាថា **"dig-ging-in-to"** (/ˈdɪɡ.ɪŋ-ɪn.tuː/)
  - **what's going on** -> និយាយភ្ជាប់គ្នាថា **"whats-goi-ning-on"** (/wɒts-ˈɡəʊ.ɪŋ-ɒn/)
* **💬 អត្ថន័យជាភាសាខ្មែរ (Khmer Meaning):**
  - *«សួស្តីអ្នកទាំងអស់គ្នា ពេលនេះ production គាំងហើយ។ Payment service គាំងទាំងស្រុងតែម្តង ហើយ users កំពុងជួបប្រទះ error 502។ ខ្ញុំកំពុងសម្រុកពិនិត្យមើល logs ឥឡូវនេះ ដើម្បីស្វែងរកមូលហេតុថាមានបញ្ហាអ្វីកើតឡើង។»*

---

## 🗣️ ស្គ្រីបទី ២៖ ការរាយការណ៍វឌ្ឍនភាពនៃការដោះស្រាយ (Providing updates)

### 💼 Professional Version
> "An update on the production issue: We identified that the database connection pool was full. We have increased the pool limit and restarted the service. The system is back online."

### 🔥 Natural/Casual Version (Slay!)
> "Quick update on the database issue: **Turns out** the DB connection pool was **maxed out**. We've **bumped up the pool size** and **spun up the service again**. The app is **back up and running**."

* **🗣️ Spoken & Linking Guide (គន្លឹះភ្ជាប់សំឡេង):**
  - **turns out** -> និយាយភ្ជាប់គ្នាថា **"turn-zout"** (/tɜːnz-aʊt/)
  - **maxed out** -> និយាយភ្ជាប់គ្នាថា **"mak-stout"** (/mækst-aʊt/)
  - **bumped up** -> និយាយភ្ជាប់គ្នាថា **"bum-ptup"** (/bʌmpt-ʌp/)
  - **back up and** -> និយាយភ្ជាប់គ្នាថា **"bak-ku-pan"** (/bæk-ʌp-ænd/)
* **💬 អត្ថន័យជាភាសាខ្មែរ (Khmer Meaning):**
  - *«បច្ចុប្បន្នភាពខ្លីអំពីបញ្ហា database៖ រកឃើញថា DB connection pool ត្រូវបានពេញហៀរដល់ដែនកំណត់។ យើងបានបង្កើនទំហំ pool និងបានដំណើរការ service ឡើងវិញ។ កម្មវិធីអាចដំណើរការឡើងវិញជាធម្មតាហើយ។»*

---

## 🗣️ ស្គ្រីបទី ៣៖ របាយការណ៍ក្រោយការដោះស្រាយ (Post-Incident summary)

### 💼 Professional Version
> "The issue has been completely resolved. The root cause was an unindexed query. I have added the database indexes. I will write a post-mortem report today."

### 🔥 Natural/Casual Version (Slay!)
> "The issue is **fully resolved**. The culprit was a **missing DB index** on orders, which **slowed everything down**. I've **added the index**, and latency is **back to normal**. I'll **put together a post-mortem** this afternoon."

* **🗣️ Spoken & Linking Guide (គន្លឹះភ្ជាប់សំឡេង):**
  - **fully resolved** -> និយាយលឿនៗថា **"ful-ly-re-zolvd"**
  - **slowed everything** -> និយាយភ្ជាប់គ្នាថា **"slow-dev-ry-thing"** (/sləʊd-ˈev.ri.θɪŋ/)
  - **put together** -> និយាយលឿនៗថា **"put-t'ge-ther"**
* **💬 អត្ថន័យជាភាសាខ្មែរ (Khmer Meaning):**
  - *«បញ្ហាត្រូវបានដោះស្រាយទាំងស្រុងហើយ។ ដើមចមនៃបញ្ហាគឺមកពី orders table គ្មាន database index ដែលធ្វើឱ្យរាល់ transaction ដំណើរការយឺតខ្លាំង។ ខ្ញុំបានបន្ថែម index រួចហើយ ហើយល្បឿន latency បានត្រឡប់មកធម្មតាវិញហើយ។ ខ្ញុំនឹងចងក្រងសរសេរ post-mortem report នៅរសៀលនេះ។»*

---
🔗 **[ត្រឡប់ទៅមេរៀនមុន (Back to Module Index)](../README.md)**
