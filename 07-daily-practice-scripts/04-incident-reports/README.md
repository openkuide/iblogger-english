# Handling Incident Reports (ស្គ្រីបរាយការណ៍បញ្ហាបន្ទាន់)

ស្គ្រីបរាយការណ៍បញ្ហាប្រព័ន្ធគាំង ឬមាន bug ធ្ងន់ធ្ងរនៅលើ production។

Incident communication templates for reporting bugs and server crashes on production.

---

## 🗣️ ស្គ្រីបទី ១៖ ការរាយការណ៍បញ្ហាដំបូងបង្អស់ (Reporting the incident)

### 💼 Professional Version
> "Hi everyone, we have a critical incident on production. The payment service is currently unresponsive. I am investigating the logs right now to identify the root cause."

### 🔥 Natural/Casual Version (Slay!)
> "Hey guys, **production is down** right now. The **payment service is completely locked up**, and users are getting 502 errors. I'm **digging into the logs** as we speak to **figure out what's going on**."

* **Key Vocabulary:**
  - *production is down:* ប្រព័ន្ធគាំង/លែងដំណើរការ (instead of *critical incident on production*)
  - *completely locked up:* គាំងទាំងស្រុង/គាំងលែងឆ្លើយតប (instead of *unresponsive*)
  - *digging into:* សម្រុកឆែកមើលយ៉ាងស៊ីជម្រៅ (instead of *investigating*)
  - *figure out what's going on:* រកមើលថាមានបញ្ហាអ្វីកើតឡើង (instead of *identify the root cause*)

---

## 🗣️ ស្គ្រីបទី ២៖ ការរាយការណ៍វឌ្ឍនភាពនៃការដោះស្រាយ (Providing updates)

### 💼 Professional Version
> "An update on the production issue: We identified that the database connection pool was full. We have increased the pool limit and restarted the service. The system is back online."

### 🔥 Natural/Casual Version (Slay!)
> "Quick update on the database issue: **Turns out** the DB connection pool was **maxed out**. We've **bumped up the pool size** and **spun up the service again**. The app is **back up and running**."

* **Key Vocabulary:**
  - *turns out:* រកឃើញថា/មកពី (instead of *we identified*)
  - *maxed out:* ពេញហៀរ/ដល់ដែនកំណត់ (instead of *full*)
  - *bumped up:* ដំឡើង/បង្កើន (instead of *increased*)
  - *spun up:* ចាប់ផ្តើមដំណើរការឡើងវិញ (instead of *restarted*)
  - *back up and running:* ដំណើរការឡើងវិញជាធម្មតា (instead of *back online*)

---

## 🗣️ ស្គ្រីបទី ៣៖ របាយការណ៍ក្រោយការដោះស្រាយ (Post-Incident summary)

### 💼 Professional Version
> "The issue has been completely resolved. The root cause was an unindexed query. I have added the database indexes. I will write a post-mortem report today."

### 🔥 Natural/Casual Version (Slay!)
> "The issue is **fully resolved**. The culprit was a **missing DB index** on orders, which **slowed everything down**. I've **added the index**, and latency is **back to normal**. I'll **put together a post-mortem** this afternoon."

* **Key Vocabulary:**
  - *culprit:* មូលហេតុចម្បងបង្កបញ្ហា (instead of *root cause*)
  - *slowed everything down:* ធ្វើឱ្យគ្រប់យ៉ាងដំណើរការយឺត (instead of *caused slow transactions*)
  - *put together:* ចងក្រង/សរសេរ (instead of *write*)

---
🔗 **[ត្រឡប់ទៅមេរៀនមុន (Back to Module Index)](../README.md)**
