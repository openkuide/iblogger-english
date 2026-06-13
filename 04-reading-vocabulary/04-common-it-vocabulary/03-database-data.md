# Database & Data Vocabulary (កម្រងវាក្យសព្ទ Database & ទិន្នន័យ)

កម្រងវាក្យសព្ទគន្លឹះចំនួន ១០០ សម្រាប់ផ្នែក Database, SQL, ORM, JPA, JSON និងការគ្រប់គ្រងទិន្នន័យ។

A list of 100 essential vocabulary words for Database design, SQL queries, transaction properties, and ORM mapping.

---

| No. | Word (ពាក្យ) | POS | Khmer Translation (អត្ថន័យ) | Example Sentence |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **query** | Noun/V | សំនួរទាញទិន្នន័យ / សួរទិន្នន័យ | Run the SELECT query to fetch active users. |
| 2 | **migration** | Noun | ការកែប្រែ/ផ្លាស់ប្តូរ schema មូលដ្ឋានទិន្នន័យ | The database migration failed due to constraint. |
| 3 | **schema** | Noun | រចនាសម្ព័ន្ធតារាងមូលដ្ឋានទិន្នន័យ | We modified the user table schema. |
| 4 | **index** | Noun/V | សន្ទស្សន៍ជួយស្វែងរកលឿន / បង្កើតសន្ទស្សន៍ | Index the email column to optimize lookup speed. |
| 5 | **redundancy** | Noun | ភាពស្ទួនគ្នានៃទិន្នន័យ | Database normalization reduces redundancy. |
| 6 | **constraint** | Noun | លក្ខខណ្ឌបង្ខំ/ដែនកំណត់លើទិន្នន័យ | Violating foreign key constraint throws error. |
| 7 | **transaction** | Noun | ប្រតិបត្តិការទិន្នន័យ | The transaction committed successfully. |
| 8 | **cache** | Noun/V | អង្គចងចាំបណ្តោះអាសន្នល្បឿនលឿន | Cache query results to improve speed performance. |
| 9 | **retrieve** | Verb | ទាញយក/នាំយកទិន្នន័យមកវិញ | Retrieve user details from the database. |
| 10 | **populate** | Verb | បញ្ចូលទិន្នន័យបំពេញតារាង | Populate the database with default admin data. |
| 11 | **table** | Noun | តារាងផ្ទុកទិន្នន័យ | The users table contains ten columns. |
| 12 | **column** | Noun | ជួរឈរនៃតារាង | The status column stores integer values. |
| 13 | **row / record** | Noun | ជួរដេក ឬកំណត់ត្រាទិន្នន័យមួយ | Insert a new record into the database. |
| 14 | **key** | Noun | កូនសោសម្គាល់ទិន្នន័យ (primary/foreign) | Define user id as the primary key. |
| 15 | **primary key** | Noun | កូនសោចម្បងសម្គាល់ជួរដេកនីមួយៗមិនឱ្យជាន់គ្នា | The primary key must be unique and non-null. |
| 16 | **foreign key** | Noun | កូនសោចម្លងសម្រាប់ភ្ជាប់ទំនាក់ទំនងតារាង | The foreign key links orders to users table. |
| 17 | **unique** | Adj | ដែលមានតម្លៃតែមួយគត់មិនជាន់គ្នា | The email field must have a unique index constraint. |
| 18 | **null** | Adj/N | ដែលគ្មានតម្លៃ ឬទទេស្អាត | The description field can be null. |
| 19 | **nullable** | Adj | ដែលអនុញ្ញាតឱ្យមានតម្លៃ null បាន | Set the nickname column as nullable. |
| 20 | **normalization**| Noun | ដំណើរការរៀបចំកាត់បន្ថយភាពស្ទួនទិន្នន័យ | Database normalization improves data integrity. |
| 21 | **denormalization**| Noun | ដំណើរការបញ្ច្រាសដើម្បីល្បឿនអានលឿនជាង | Denormalization is used in data warehousing. |
| 22 | **integrity** | Noun | ភាពត្រឹមត្រូវអភិរក្ស និងសុពលភាពទិន្នន័យ | Foreign key constraint ensures data integrity. |
| 23 | **consistency** | Noun | ភាពស៊ីសង្វាក់គ្នានៃទិន្នន័យក្នុងប្រព័ន្ធ | ACID guarantees data consistency after transactions. |
| 24 | **isolation** | Noun | ភាពដាច់ដោយឡែកគ្នានៃប្រតិបត្តិការស្របគ្នា | Isolation prevents transactions from interfering. |
| 25 | **durability** | Noun | ភាពរឹងមាំជាប់ជានិច្ចក្រោយរក្សាទុក | Durability ensures database commits survive crashes. |
| 26 | **ACID** | Noun | បណ្តុំលក្ខណៈសម្បត្តិលំនឹង database | Relational databases comply with ACID. |
| 27 | **commit** | Verb/N | រក្សាទុកបម្រែបម្រួលជាអចិន្ត្រៃយ៍ | Commit the changes to save user records. |
| 28 | **rollback** | Verb/N | ត្រឡប់ប្រព័ន្ធទៅស្ថានភាពដើមមុនកែប្រែ | Rollback the transaction if connection fails. |
| 29 | **relational** | Adj | ដែលទាក់ទងគ្នា (Database មានតារាងភ្ជាប់គ្នា) | PostgreSQL is a relational database. |
| 30 | **NoSQL** | Noun | Database មិនប្រើប្រាស់ SQL (ដូចជា document/key-value) | MongoDB is a popular NoSQL database. |
| 31 | **document** | Noun | ទម្រង់ទិន្នន័យ NoSQL (ដូចជា JSON) | MongoDB stores records as document objects. |
| 32 | **collection** | Noun | តារាង NoSQL (បណ្តុំ documents) | The users collection contains user profiles. |
| 33 | **join** | Noun/V | ការភ្ជាប់តារាងពីរ ឬច្រើនដើម្បីទាញទិន្នន័យ | Use inner join to retrieve order details. |
| 34 | **aggregate** | Verb/Adj | បូកសរុប ឬចងក្រង (SUM, AVG, COUNT) | Use aggregate functions to calculate sales. |
| 35 | **procedure** | Noun | នីតិវិធីរក្សាទុកក្នុង database (Stored Procedure) | Execute the stored procedure to delete users. |
| 36 | **trigger** | Noun/V | កូដស្វ័យប្រវត្តិដំណើរការពេលមានការផ្លាស់ប្តូរ | The database trigger logs all updates automatically. |
| 37 | **view** | Noun | តារាងនិម្មិតកើតពី query | Create a database view for the reporting dashboard. |
| 38 | **index scan** | Noun | ការស្កេនទិន្នន័យតាម index (លឿន) | Index scan is faster than sequential scan. |
| 39 | **table scan** | Noun | ការស្កេនគ្រប់ជួរដេកទាំងអស់នៃតារាង (យឺត) | Avoid table scan by creating index tags. |
| 40 | **execution plan**| Noun | ផែនការដោះស្រាយ query របស់ database engine | Analyze the execution plan using EXPLAIN command. |
| 41 | **explain** | Verb | ពន្យល់ ឬបង្ហាញជំហានដោះស្រាយ | Explain the select query to debug slowness. |
| 42 | **pool** | Noun | អាងផ្ទុក connections បម្រុងទុក | The database connection pool was exhausted. |
| 43 | **starvation** | Noun | ស្ថានភាពដាច់ធនធានបន្តិចម្តងៗ | High traffic caused connection pool starvation. |
| 44 | **deadlock** | Noun | ស្ថានភាពស្ទះរង់ចាំចាក់សោគ្នាទៅវិញទៅមក | Resolve the database deadlock by changing query order. |
| 45 | **lock** | Noun/V | ការចាក់សោរារាំងមិនឱ្យកែប្រែទិន្នន័យ | Acquire a row lock during database update. |
| 46 | **optimistic** | Adj | របៀបគ្រប់គ្រង lock សន្មតថាគ្មានជាន់គ្នា | Use optimistic locking to prevent concurrency. |
| 47 | **pessimistic** | Adj | របៀបគ្រប់គ្រង lock សន្មតថាមានជាន់គ្នាជានិច្ច | Pessimistic locking blocks database reads. |
| 48 | **dirty read** | Noun | ការអានទិន្នន័យមិនទាន់ commit | Dirty reads are avoided in READ COMMITTED mode. |
| 49 | **isolation level**| Noun | កម្រិតដាច់ដោយឡែកនៃ transaction | Set the transaction isolation level to serializable. |
| 50 | **cascade** | Verb/Adj | ហូរធ្លាក់ចុះក្រោមតាមលំដាប់លំដោយ | Cascade delete removes orders when user is deleted. |
| 51 | **orphan** | Noun/Adj | ទិន្នន័យកំព្រា (គ្មានទំនាក់ទំនង parent) | Clean up orphan records regularly. |
| 52 | **truncate** | Verb | លុបទិន្នន័យទាំងអស់ក្នុងតារាងភ្លាមៗ (លឿនជាង delete) | Truncate the log table to free disk space. |
| 53 | **upsert** | Verb/N | ធ្វើបច្ចុប្បន្នភាពបើមាន បើគ្មានបញ្ចូលថ្មី (Update + Insert) | Execute an upsert query to update user preferences. |
| 54 | **JSON** | Noun | ទម្រង់ទិន្នន័យអត្ថបទ JavaScript Object Notation | Parse the JSON response body. |
| 55 | **XML** | Noun | ទម្រង់ទិន្នន័យអត្ថបទប្រើ tags eXtensible Markup Language | Maven configurations are written in XML formats. |
| 56 | **ORM (Object-Relational Mapping)** | Noun | ការភ្ជាប់ object កូដទៅនឹងតារាង database | Hibernate is a popular ORM tool. |
| 57 | **JPA (Java Persistence API)** | Noun | ពិធីការស្តង់ដារ Java សម្រាប់ ORM | Spring Boot implements JPA for database tasks. |
| 58 | **entity** | Noun | ថ្នាក់កូដតំណាងឱ្យតារាងមូលដ្ឋានទិន្នន័យ | Annotate the class with @Entity key. |
| 59 | **repository** | Noun | ស្រទាប់កូដចាត់ចែងទិន្នន័យ database | Extends JpaRepository to query records. |
| 60 | **data source** | Noun | ប្រភពតភ្ជាប់ទិន្នន័យ | Configure the database data source URL. |
| 61 | **driver** | Noun | កម្មវិធីបញ្ជាតភ្ជាប់ (ដូចជា JDBC Driver) | Download the PostgreSQL JDBC driver. |
| 62 | **dialect** | Noun | គ្រាមភាសា SQL របស់ database នីមួយៗ | Configure the hibernate dialect for PostgreSQL. |
| 63 | **persistence** | Noun | ភាពគង់វង់អចិន្ត្រៃយ៍នៃទិន្នន័យ | Persistence layer handles file configuration saving. |
| 64 | **migration script**| Noun | កូដកែសម្រួល schema មូលដ្ឋានទិន្នន័យ | Run the Flyway migration script setup. |
| 65 | **seeding** | Noun | ការចាក់បញ្ចូលទិន្នន័យសាកល្បងដំបូង | Seeding the user database takes a minute. |
| 66 | **denormalized**| Adj | ដែលមិនរៀបចំកាត់បន្ថយស្ទួន | Denormalized tables speed up read operations. |
| 70 | **partitioning**| Noun | ការបែងចែកតារាងធំជាបំណែកតូចៗ | Table partitioning improves big data query performance. |
| 71 | **sharding** | Noun | ការបែងចែក database ដាក់លើ servers ផ្សេងគ្នា | Database sharding distributes storage weight. |
| 72 | **replication** | Noun | ការចម្លងទិន្នន័យទុកជា backup លើ server ច្រើន | Database replication ensures high availability. |
| 73 | **master-slave** | Noun/Adj | ស្ថាបត្យកម្មប្រព័ន្ធចម្បង-រង | Write requests go to master database pool. |
| 74 | **read-heavy** | Adj | ដែលផ្តោតលើការអានទិន្នន័យច្រើនជាងសរសេរ | Configure replica DBs for read-heavy systems. |
| 75 | **write-heavy** | Adj | ដែលផ្តោតលើការសរសេរទិន្នន័យច្រើន | The log service is a write-heavy application. |
| 76 | **normalization**| Noun | បរិសុទ្ធកម្មទិន្នន័យ | Apply third normal form for normalization. |
| 77 | **foreign key** | Noun | សោរងតំណភ្ជាប់ | Define the foreign key relationship. |
| 78 | **index creation**| Noun | ការបង្កើត index | Index creation takes time on huge tables. |
| 79 | **query execution**| Noun | ការរត់សំនួរទិន្នន័យ | Query execution timed out on the production server. |
| 80 | **concurrency control**| Noun | ការគ្រប់គ្រងការកែទិន្នន័យជាន់គ្នា | Implement pessimistic concurrency control logic. |
| 81 | **backup** | Noun/V | ចម្លងរក្សាទុកបម្រុងការពារបាត់បង់ | Create a daily database backup archive. |
| 82 | **restore** | Verb | សង្គ្រោះទិន្នន័យពី backup មកវិញ | Restore the database after system crash. |
| 83 | **dump** | Noun/V | ឯកសារទិន្នន័យដែលទាញចេញទាំងអស់ | Export the database schema as a SQL dump. |
| 84 | **corruption** | Noun | ភាពខូចខាតទិន្នន័យ | Hardware failure led to database table corruption. |
| 85 | **integrity check**| Noun | ការពិនិត្យផ្ទៀងផ្ទាត់សុពលភាពទិន្នន័យ | Run an integrity check on database boot. |
| 86 | **foreign constraints**| Noun | ដែនកំណត់សោរង | Disable foreign constraints during schema wipe. |
| 87 | **entity mapping**| Noun | ការភ្ជាប់ទំនាក់ទំនង entity | Verify the Hibernate entity mapping setup. |
| 88 | **eager fetch** | Noun/Adj | ការទាញទិន្នន័យភ្ជាប់ភ្លាមៗទាំងអស់ | Eager fetch loads child records automatically. |
| 89 | **lazy fetch** | Noun/Adj | ការទាញទិន្នន័យភ្ជាប់ទាល់តែហៅទើប load | Lazy fetch prevents unnecessary database weight. |
| 90 | **N+1 query** | Noun | បញ្ហា query លើសដោយសារ loop ទាញទិន្នន័យ | Resolve the N+1 query problem using join fetch. |
| 91 | **criteria query**| Noun | របៀបសរសេរ query ដោយប្រើ Java Objects | Criteria query allows dynamic query building. |
| 92 | **native query** | Noun | សំណេរ SQL ផ្ទាល់ខ្លួនមិនប្រើ ORM abstraction | Write a native query to access database properties. |
| 93 | **stored procedure**| Noun | នីតិវិធីរក្សាទុកក្នុង DB | Call the stored procedure using Spring @Procedure. |
| 94 | **caching layer** | Noun | ស្រទាប់រក្សាទុកទិន្នន័យបណ្តោះអាសន្ន | Add a caching layer to avoid direct DB load. |
| 95 | **cache eviction**| Noun | ការសម្អាត cache ចាស់ៗចោល | Cache eviction is triggered when data changes. |
| 96 | **invalidation** | Noun | ការធ្វើឱ្យលែងមានសុពលភាព (cache/session) | Session invalidation occurs after logout. |
| 97 | **read replica** | Noun | database ចម្លងសម្រាប់តែអានទិន្នន័យ | Point reporting queries to the read replica server. |
| 98 | **failover** | Noun/V | ផ្ទេរការងារទៅ database បម្រុងពេលអាធំគាំង | Automated failover ensures high database availability. |
| 99 | **normalization levels**| Noun | កម្រិតនៃការធ្វើ normalization | Study the normalization levels before database setup. |
| 100| **integrity checks**| Noun | ការផ្ទៀងផ្ទាត់ភាពត្រឹមត្រូវ | Perform integrity checks before release deployment. |

---
🔗 **[ត្រឡប់ទៅមេរៀនមុន (Back to Module Index)](../README.md)**
