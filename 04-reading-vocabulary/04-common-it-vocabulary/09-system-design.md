# System Design & Architecture Vocabulary (វាក្យសព្ទ System Design & Architecture)

100 essential words for System Design, Architecture patterns, and High-Level Design discussions in IT teams.

---

## 🏗️ Part 1: Architecture Patterns & Monolith vs Microservices (Words 1–25)

| # | Word | Tense / Form | Khmer Meaning | Example Sentence |
|---|------|-------------|---------------|-----------------|
| 1 | **architecture** | n. | ស្ថាបត្យកម្មប្រព័ន្ធ | The software *architecture* determines system scale. |
| 2 | **monolith** | n. (monoliths) | monolith (ប្រព័ន្ធរួមតែមួយ) | Migrating from a *monolith* to microservices takes time. |
| 3 | **microservices** | n. | microservices (ប្រព័ន្ធបំបែកតូចៗ) | *Microservices* allow teams to deploy independently. |
| 4 | **decouple** | v. (decoupled, decoupling) | បំបែកទំនាក់ទំនងកុំឱ្យជាប់គ្នា | *Decouple* the billing service from the user service. |
| 5 | **coupling** | n. | ការផ្សារភ្ជាប់គ្នា | High *coupling* makes code hard to modify. |
| 6 | **cohesion** | n. | ភាពស្អិតរមួត / ភាពពាក់ព័ន្ធគ្នានៃមុខងារ | Aim for high *cohesion* inside modules. |
| 7 | **service-oriented** | adj. (SOA) | ដែលផ្អែកលើសេវាកម្ម | Our old system was built on a *service-oriented* model. |
| 8 | **distributed** | adj. | ដែលបែងចែក / ចែកចាយ | Debugging *distributed* systems is challenging. |
| 9 | **centralized** | adj. | ដែលប្រមូលផ្តុំនៅកណ្តាល | A *centralized* database handles all writes. |
| 10 | **decentralized** | adj. | ដែលមិនប្រមូលផ្តុំ / ចែកចាយ | Blockchain is a *decentralized* network. |
| 11 | **peer-to-peer** | adj. (P2P) | ពីឧបករណ៍មួយទៅឧបករណ៍មួយដោយផ្ទាល់ | Git uses a *peer-to-peer* architecture. |
| 12 | **client-server** | adj./n. | ម៉ាស៊ីនភ្ញៀវនិងម៉ាស៊ីនបម្រើ | Web apps use the traditional *client-server* pattern. |
| 13 | **event-driven** | adj. | ដែលដំណើរការតាមព្រឹត្តិការណ៍ | *Event-driven* architecture uses messages for communication. |
| 14 | **message queue** | n. (message queues) | ជួររង់ចាំសារ | We use RabbitMQ as our *message queue*. |
| 15 | **broker** | n. (brokers) | តំណាងសម្របសម្រួល / broker | Kafka acts as the message *broker*. |
| 16 | **publish-subscribe**| n./v. (pub/sub) | គំរូផ្សាយនិងចុះឈ្មោះទទួល | Use the *publish-subscribe* model to broadcast updates. |
| 17 | **publisher** | n. (publishers) | អ្នកផ្សាយព័ត៌មាន | The order service is the *publisher* of the event. |
| 18 | **subscriber** | n. (subscribers) | អ្នកទទួលព័ត៌មាន | The email service is a *subscriber* to 'OrderCreated'. |
| 19 | **asynchronous** | adj. (async) | មិនស្របពេលគ្នា | *Asynchronous* tasks don't block the main thread. |
| 20 | **synchronous** | adj. (sync) | ស្របពេលគ្នា | HTTP requests are typically *synchronous*. |
| 21 | **stateless** | adj. | គ្មានការរក្សាទុកស្ថានភាព | REST APIs should be *stateless* for easy scaling. |
| 22 | **stateful** | adj. | មានការរក្សាទុកស្ថានភាព | Databases are *stateful* applications. |
| 23 | **gateway** | n. (gateways) | ច្រកទ្វាររួម | The API *gateway* routes client requests. |
| 24 | **orchestrator** | n. (orchestrators) | អ្នកគ្រប់គ្រងសម្របសម្រួល | The workflow *orchestrator* runs background jobs. |
| 25 | **choreography** | n. | ការរៀបចំដោយខ្លួនឯងគ្មានអ្នកបញ្ជា | Event *choreography* avoids tight coupling. |

---

## ⚡ Part 2: Scalability, Performance & Reliability (Words 26–50)

| # | Word | Tense / Form | Khmer Meaning | Example Sentence |
|---|------|-------------|---------------|-----------------|
| 26 | **scaling** | n. | ការពង្រីកទំហំប្រព័ន្ធ | Horizontal *scaling* adds more server instances. |
| 27 | **vertical scaling** | n. (scaling up) | ការពង្រីកទំហំឡើងលើ (បន្ថែម CPU/RAM) | *Vertical scaling* is limited by hardware capacity. |
| 28 | **horizontal scaling**| n. (scaling out) | ការពង្រីកទំហំទៅចំហៀង (ថែម server) | *Horizontal scaling* is preferred for cloud apps. |
| 29 | **throughput** | n. | ចំនួនប្រតិបត្តិការក្នុងមួយវិនាទី | Measure system *throughput* during load tests. |
| 30 | **latency** | n. | រយៈពេលរង់ចាំឆ្លើយតប | Our goal is to keep API *latency* under 100ms. |
| 31 | **bottleneck** | n. (bottlenecks) | ចំណុចស្ទះ | The database index was the performance *bottleneck*. |
| 32 | **availability** | n. | ភាពអាចប្រើប្រាស់បាន | High *availability* systems have multi-zone backups. |
| 33 | **fault tolerance** | n. | ភាពធន់នឹងកំហុស | System *fault tolerance* keeps the app alive during outages. |
| 34 | **redundancy** | n. | ភាពស្ទួនការពារទុកជាមុន | *Redundancy* is essential for mission-critical systems. |
| 35 | **replication** | n. | ការចម្លងទិន្នន័យដូចគ្នា | Set up database *replication* for read scaling. |
| 36 | **failover** | n. / v. (failed over) | ការប្តូរទៅម៉ាស៊ីនបម្រុងពេលខូច | Test automatic *failover* in staging. |
| 37 | **partitioning** | n. | ការបែងចែកទិន្នន័យ | Table *partitioning* improves query performance. |
| 38 | **sharding** | n. | ការបំបែកទិន្នន័យដាក់ម៉ាស៊ីនផ្សេងគ្នា | *Sharding* the DB helped us scale past write limits. |
| 39 | **consistent hashing**| n. | consistent hashing (ក្បួនចែកចាយទិន្នន័យ) | *Consistent hashing* minimizes cache misses during re-scaling. |
| 40 | **load balancing** | n. | ការបែងចែកបន្ទុកការងារ | *Load balancing* distributes traffic evenly. |
| 41 | **clustering** | n. | ការចងក្រងជាក្រុម | A Kubernetes *clustering* setup runs our containers. |
| 42 | **rate limiting** | n. | ការកំណត់ចំនួនដងនៃការហៅចូល | Implement *rate limiting* to protect the API from abuse. |
| 43 | **throttling** | n. | ការកាត់បន្ថយល្បឿនដំណើរការ | *Throttling* slows down users who exceed their limit. |
| 44 | **circuit breaker** | n. (circuit breakers) | ឧបករណ៍កាត់ផ្តាច់ស្វ័យប្រវត្តិពេលមានកំហុស | Use the *circuit breaker* pattern to handle external API timeouts. |
| 45 | **fallback** | n. (fallbacks) | គម្រោងឬទិន្នន័យបម្រុង | Define a *fallback* method when payment fails. |
| 46 | **heartbeat** | n. (heartbeats) | សញ្ញាបញ្ជាក់ថាប្រព័ន្ធកំពុងដំណើរការ | The server sends a *heartbeat* to the coordinator. |
| 47 | **health check** | n. (checks) | ការត្រួតពិនិត្យសុខភាពប្រព័ន្ធ | The load balancer calls the *health check* endpoint. |
| 48 | **graceful degradation**| n. | ការកាត់បន្ថយមុខងារមិនសំខាន់ដើម្បីរក្សាប្រព័ន្ធ | *Graceful degradation* keeps search active even if recommendations fail. |
| 49 | **outage** | n. (outages) | ការគាំង/ការដាច់ប្រព័ន្ធ | The data center *outage* lasted two hours. |
| 50 | **downtime** | n. | រយៈពេលប្រព័ន្ធឈប់ដំណើរការ | Our scheduled maintenance *downtime* is at midnight. |

---

## 💾 Part 3: Data Management & Caching (Words 51–75)

| # | Word | Tense / Form | Khmer Meaning | Example Sentence |
|---|------|-------------|---------------|-----------------|
| 51 | **caching** | n. | ការរក្សាទុកបណ្តោះអាសន្ន | Use Redis for session *caching*. |
| 52 | **cache hit** | n. (cache hits) | ការរកឃើញទិន្នន័យក្នុង cache | A high *cache hit* ratio speeds up the app. |
| 53 | **cache miss** | n. (cache misses) | ការរកមិនឃើញទិន្នន័យក្នុង cache | A *cache miss* requires querying the database. |
| 54 | **eviction** | n. | ការដកចេញពី cache | Configure LRU *eviction* policy. |
| 55 | **invalidation** | n. | ការធ្វើឱ្យលែងមានតម្លៃប្រើការ | Cache *invalidation* is a hard problem. |
| 56 | **write-through** | adj. | សរសេរចូល cache និង DB ស្របគ្នា | Use *write-through* cache for instant updates. |
| 57 | **write-back** | adj. (write-behind) | សរសេរចូល cache រួចសរសេរចូល DB តាមក្រោយ | *Write-back* cache improves write performance. |
| 58 | **read-through** | adj. | អានពី cache បើគ្មានអានពី DB មកដាក់ | Implement *read-through* caching for catalog data. |
| 59 | **CDN** | abbr. (Content Delivery Network) | បណ្តាញចែកចាយមាតិការហ័ស | Cache images and scripts on a *CDN*. |
| 60 | **edge cache** | n. | cache នៅជិតអ្នកប្រើបំផុត | CDNs use *edge cache* to reduce latency. |
| 61 | **NoSQL** | adj./n. | គ្រឹះទិន្នន័យមិនមែន SQL | Use *NoSQL* for unstructured data. |
| 62 | **RDBMS** | abbr. | គ្រឹះទិន្នន័យទំនាក់ទំនង | PostgreSQL is a powerful *RDBMS*. |
| 63 | **schema-less** | adj. | គ្មានទម្រង់កំណត់តឹងរ៉ឹង | MongoDB is *schema-less*. |
| 64 | **denormalization** | n. | ការបញ្ចូលតារាងដើម្បីល្បឿនអាន | *Denormalization* improves read speeds in NoSQL. |
| 65 | **ACID** | abbr. | លក្ខណៈធានានៃប្រត្តិការ (RDBMS) | relational databases guarantee *ACID* properties. |
| 66 | **BASE** | abbr. | លក្ខណៈធានាក្នុងប្រព័ន្ធចែកចាយ | NoSQL databases follow *BASE* consistency. |
| 67 | **eventual consistency**| n. | ភាពស៊ីសង្វាក់គ្នានៅទីបំផុត | DynamoDB offers *eventual consistency*. |
| 68 | **strong consistency**| n. | ភាពស៊ីសង្វាក់គ្នាភ្លាមៗ | Financial apps require *strong consistency*. |
| 69 | **CAP theorem** | n. | ទ្រឹស្ដីបទ CAP | The *CAP theorem* says you can only choose two. |
| 70 | **partition tolerance**| n. | ភាពធន់នឹងការដាច់បណ្តាញ | *Partition tolerance* is required in distributed apps. |
| 71 | **data store** | n. (data stores) | ឃ្លាំងផ្ទុកទិន្នន័យ | Elasticsearch is our primary search *data store*. |
| 72 | **migration** | n. (migrations) | ការប្តូរទម្រង់/ផ្លាស់ទីទិន្នន័យ | Run the database schema *migration*. |
| 73 | **data lake** | n. (data lakes) | ធុងផ្ទុកទិន្នន័យឆៅដ៏ធំ | Analytics tools process data from the *data lake*. |
| 74 | **warehouse** | n. (warehouses) | ឃ្លាំងទិន្នន័យសម្រេច | Query the data *warehouse* for quarterly reports. |
| 75 | **ETL** | abbr. (Extract, Transform, Load) | ដំណើរការទាញ 转换 និងផ្ទុក | The *ETL* pipeline runs every midnight. |

---

## 📐 Part 4: Design Principles & Integration (Words 76–100)

| # | Word | Tense / Form | Khmer Meaning | Example Sentence |
|---|------|-------------|---------------|-----------------|
| 76 | **scalability** | n. | ភាពអាចពង្រីកបាន | Design for *scalability* from day one. |
| 77 | **loose coupling** | n. | ការភ្ជាប់គ្នាធូរស្រាល (មិនតឹងរ៉ឹង) | *Loose coupling* enables modular updates. |
| 78 | **tight coupling** | n. | ការភ្ជាប់គ្នាស្អិតរមួត (កែមួយខូចមួយទៀត) | Avoid *tight coupling* between database models. |
| 79 | **separation of concerns**| n. | ការបំបែកភារកិច្ចដាច់ដោយឡែក | MVC pattern follows *separation of concerns*. |
| 80 | **DRY** | abbr. (Don't Repeat Yourself) | កុំសរសេរកូដដដែលៗ | Follow *DRY* principle to reduce code duplication. |
| 81 | **KISS** | abbr. (Keep It Simple, Stupid) | រក្សាវាឱ្យសាមញ្ញបំផុត | Apply the *KISS* principle during architecture reviews. |
| 82 | **YAGNI** | abbr. (You Aren't Gonna Need It) | កុំសរសេរកូដដែលមិនទាន់ត្រូវការ | Don't build auto-scaling now; follow *YAGNI*. |
| 83 | **idempotency** | n. | ភាពធ្វើដដែលលទ្ធផលដដែល | Payment APIs require strict *idempotency*. |
| 84 | **statelessness** | n. | ភាពគ្មានការចាំស្ថានភាព | App tier *statelessness* simplifies horizontal scaling. |
| 85 | **single point of failure**| n. (SPOF) | ចំណុចខូចមួយនាំឱ្យខូចទាំងស្រុង | A single database server is a *single point of failure*. |
| 86 | **backpressure** | n. | សម្ពាធត្រឡប់មកវិញ | Use buffering to handle consumer *backpressure*. |
| 87 | **rate limiter** | n. (limiters) | ឧបករណ៍កម្រិតដងនៃការហៅចូល | Add a *rate limiter* to prevent API abuse. |
| 88 | **dead letter queue**| n. (DLQ) | ជួររង់ចាំសារមានបញ្ហា | Unprocessed events are sent to a *dead letter queue*. |
| 89 | **message bus** | n. (buses) | ផ្លូវបញ្ជូនសាររួម | The services communicate via a shared *message bus*. |
| 90 | **polling** | n. / v. (polled) | ការសួរយកព័ត៌មានដដែលៗ | Long-*polling* is replaced by WebSockets. |
| 91 | **webhook** | n. (webhooks) | ចំណុចហៅត្រឡប់ពេលមានព្រឹត្តិការណ៍ | Stripe sends payment updates via a *webhook*. |
| 92 | **gRPC** | n. | ពិធីការទំនាក់ទំនងល្បឿនលឿន | Use *gRPC* for internal microservice communication. |
| 93 | **REST** | n. / adj. | REST (ស្ថាបត្យកម្ម API) | We expose public endpoints using *REST*. |
| 94 | **GraphQL** | n. | GraphQL (ស្ថាបត្យកម្ម API) | *GraphQL* allows clients to request specific fields. |
| 95 | **serialization** | n. | ការបំប្លែងទិន្នន័យជាខ្សែអក្សរ | JSON *serialization* is standard for REST APIs. |
| 96 | **deserialization** | n. | ការបំប្លែងខ្សែអក្សរមកជាទិន្នន័យដើម | *Deserialization* fails if the JSON format is invalid. |
| 97 | **backward compatibility**| n. | ភាពអាចប្រើជាមួយកំណែចាស់បាន | Ensure *backward compatibility* when updating APIs. |
| 98 | **forward compatibility**| n. | ភាពអាចត្រូវគ្នាជាមួយកំណែអនាគត | Design schemas with *forward compatibility* in mind. |
| 99 | **monolithic architecture**| n. | ស្ថាបត្យកម្ម monolith | Our legacy app uses a *monolithic architecture*. |
| 100 | **microservices architecture**| n. | ស្ថាបត្យកម្ម microservices | Netflix pioneered *microservices architecture*. |

---

## 🗣️ Quick Phrases for System Design Discussions

| Situation | English Phrase | Khmer |
|-----------|---------------|-------|
| Pointing out a Single Point of Failure | "The single database server is a single point of failure." | "ម៉ាស៊ីន server database តែមួយគត់គឺជា Single Point of Failure។" |
| Suggesting Caching | "We should use Redis to cache these database queries." | "យើងគួរតែប្រើ Redis ដើម្បី cache database queries ទាំងនេះ។" |
| Recommending decoupling | "Let's decouple the notification system from order processing." | "ចូរយើងបំបែកប្រព័ន្ធ notification ចេញពីការដំណើរការ order។" |
| Discussing API scaling | "We need horizontal scaling to handle this traffic." | "យើងត្រូវការ horizontal scaling ដើម្បីគ្រប់គ្រង traffic នេះ។" |
| Explaining Idempotency | "Ensure the payment API is idempotent to avoid double charges." | "ធានាថា API ទូទាត់ប្រាក់មាន idempotency ដើម្បីចៀសវាងការគិតប្រាក់ពីរដង។" |

---

*Words 801–900 | Module 04 > Chapter 09*

---

### 🧠 ការអនុវត្ត និងការឆ្លុះបញ្ចាំង (Practice & Reflection)

1. **Active Retrieval (ការរំលឹកឡើងវិញ)**: Select 5 key terms from the list above that you commonly encounter in your work. Write down their meanings in your own words.
2. **Contextual Writing (ការសរសេរតាមបរិបទ)**: Write a brief paragraph (3-5 sentences) in English describing your current software development project, integrating at least 3 vocabulary words from this chapter.
3. **Reflective Discussion (ការឆ្លុះបញ្ចាំង)**: Why is using precise, standardized technical English terminology important when communicating with cross-border team members or writing documentation? How does it affect cognitive clarity in a distributed team?

---
🔗 **[ត្រឡប់ទៅមេរៀនមុន (Back to Module Index)](../README.md)**