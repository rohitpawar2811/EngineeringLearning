# Part-1

- Dependecy : spring.boot.data.jpa
- JdbcTemplate
- NamedJdbcTemplate
- Datasource Manages the Connection creation and discarding work and also handles the connection-pool.
- The database-properties we define in application.properties create this datasource 
	- spring.datasource.url =
	- spring.datasource.driver-class-name
	- spring.datasource.username
	- spring.datasource.password
- Alternatively we can init datasources by creating @Bean of Datasource and define class as @Configuarion.
- Methods query(String sql, RowMapper);
- Methods update(String sql, PreparedStatement);

# Architecture Part-2 

1. SpringBoot -> JPA(Specification) -> Hibernate(implementation we can change) -> Jdbc-Driver -> Native-DB-specific-Driver -> Mysql-DB

2. Download spring-boot-starter-data-jpa

3. @Entity : It's a java class which is equivalent to DB table.
	- The fields of the class are consider as column of table.
	- When we create 
	
	
	My current project doesn't fully leverage my skills and experience. I'm seeking a role that offers better alignment with my capabilities and growth potential
4. Persistent context manages the lifeCycle of an enity.

5. EntityManagerFactory -> EntityManager(session in terms of Hibernate) -> Persistentcontext(it will deals with entity operation and intreacts directly with Db)

6. Persistence Context also use Transaction manager internally for making the data-state consistent.

7. Like Directly EntityManager has method like -> persist, create, update, createQuery , And its implemenation is provided by the SessionImpl class of hibernate.
Why we don't use EnityManager directly instead of using JpaRepository answer is that 
	- It provides some method like findAll update etc.
	- And also Manages the EntityManager creation and close operation internally.
	- Pagination and sorting capability.
	- And like as we know operation like update/delete/modify are restricted to have Open-transaction so it will implicitly annotate all operation like that with @Transactional we don't need to specify it.

8. TransactionManger -> 
 - Resourse(Local) 1DB specific works (Java Persistent Api Transaction Manager used in this case.)
 - JTA (Java Transaction API) also called as 2Phase commit it. Like if there is 2 DB connected or involved 2 EntityManager it will commulate it in gloabal transaction. manged transaction can span across multiple Db
 SAGA VS 2Phase commit
 
 - SpringBoot Create Object of JPATransactionManager
 
 9. @Configuration class for Managing multi -> Datasource (HikariDatasource) -> JpaVendorAdaptorDatasource-> LocalContainerEntityManagerFactoryBean (EntityManager) -> TransactionManager
	
10. In the PersistentContext entity/Data wents to multiple phases like
	- Managed(PC) -> flush -> DB
	- Removed (Delete case)
	- Diattached
All operation wents through Persistent Context
	
ATomix and XADatasource	
	
	---------------------------------------------------------------------------------------
# JDBC Part-3 

First Level Caching in JPA

1. EntityManager is created for each HttpRequest, so different methods share the same EntityManger and presistent context.

2. Dispather-Servlet does this creation of EntityManager for EachRequest.

3. Calling save() method -> JpaRepository -> SimpleJpaRepository  
(It would wants the EntityManager so with the help of SessionImpl.java it provids the EntityManager object.  )

-> Inside EnitityManager (StatefulPersistenceContext) object PersistentContextMap creates or we can say cache which holds the entity.

-> And whenever we again apply the getRequest. If firstly checks for the cache if got send from there otherwise hit Db


So that's How this First level JPA cache works.
Where for every request we create separate EntityManager and they got allocated separate Persistent context not aware of other PA state. So That's how request level cache works.

-----------------------------------------------------------

# Part-3

1. In JPA Hibernate as we know 1st level cache we can only use on request-level only, So by enabling 2nd level cache we can get global-in-memory-cache which is called as 2nd level cache.

2. Now How to enable 2n level cache?
	1. Import dependency like : org.ehcache -> ehcache, org.hibernate->hibernate-jcache, javax.cache->cache-api
	2. application.properties need to specify 
		- use_second_level_cache
		- region_factory_class = hibernate-jcache
		- povider=EhcacheCachingProvider
		-spi=DEBUG
3. Architecture

	1. [Hibernate] -> 
	2. [Hibernate-cache] -> 
	3. [JCache-API Interface] ---(Implemenation)-->1. Echace 2. Caffine 3.Hazalcast


4. So there are three implemenation of cache and specification is preovide by the JCache-Api :
	1. Ecache
	2. Caffine
	3. Hazalcast
5. Here [Hibernate-cache] helps in resolving the annotations like @Cache on the entity like what would be the prefered action, so first Hibernate reads the @Cache annotation and then connect Hibernate-cache and then it will interact with JCache-Api or we can say implementations.
6. Another reason would be for running hibernate specific cache logic like CacheConcurrencyStrategy and this would hels us on it.
7. So all in all it is a bridge between hibernate and Jcache which resolves gap.

8. Jcache Provides the interface, so that hibernate interacts with cache And also provids loose-coupling.

9. Region: 
	- Help in logical grouping of cached data.
	- For each Regions(or say group), we can apply different caching strategy like
		- Eviction poicy: LiFo, Fifo, Lru, MrU
		- TTL
		- Cache size
		- Concurrency strategy etc.
	- Which helps in achieving granular level management of cached data (wither Entity, Collection or Query result)

10. @Cache(usage= CacheConcurrencyStrategy.READ_WRITE,
		region = "userDetailsCache")
	- this annotation comes at the top @Entity class 
	- Region based it will create different Cache
	- There is ehcache.xml where we can configure Eviction poicy: LiFo, Fifo, Lru, MrU
		- TTL
		- Cache size
	
11. CacheConcurrencyStrategy There are 4 types :
	1. Read_Only : It does not allow update operation on those entity. It will place a lock. Good for static Data. If try to update just entity, exception will come.
	2. Read_Write : 
		- It would allow both operation. 
		- On Read Shared lock place Other reads can aquire. But no Write operation.
		- On update puts exclusive lock deny other write and read operation.
		- Cycle : on update first on 2nd level cache mark invalidate -> update in Db -> back in 2nd level cache & update changes and unmark (If any how error comes in this process then on next read cache clean as it is alrady marked invalidate and hit db) 
	
	3. NON_STRICT_READ_WRITE : 
		- During Read No Lock is aquired at all.
		- During update, transaction commit, cache mark invalidate but not update with fresh data.
		- Good for Heavy read application
		- so if read/write happend parallel, its a chance of stale data.
	4. TRASACTIONAL
		- Lock both side read and write
		- Update the cache after trasaction
		- During Read operation found lock direclty hit DB.
		- During write operation cache-lock , waits in queue

	
		
----------------------------------------------------------------------------------
# Part-4 @Id and Autoincrrement

1. spring.jpa.hibernate.ddl-auto This would tells hibernate how to create and manage DB schema.
	- none
	- update
	- validate
	- create
	- create-drop
2. Optional @Table -> name, schema-nameUniqueKey, IndexesKey
	- If this is not defined then hibernate generate the table name by enity-class name UserDetails -> USER_DETAILS.
3. @Enity -> Tells hibernate to interlink or treat it as table.
4. @Column -> name, unique, nullable, length. Optional if not defined by var name it resolves column name.
5. @Id -> we use this to mark column as primary key.
6. Primary Key
	- Non null, unique and used to identify the column uniquely
	- Only 1 PK exists in table
	- We can @Id, @Embeddable and @EmbeddedId Vs @IdClass and @Id
	- Primary key can be composite key above annotation helps on it.
	
7. CompositeClass Making rules
	- Must be public class
	- must implement serializable : as it is custom-class that needs to send on network.
	- no-args constructor 
	- must override the equals and hashCode method ,as we are using 1st and 2nlevel cache which uses hashMap where throw PK we identify records so for that it is must.
	
8. 
@Table(name= "user_detials")
@IdClass(UserDetailsCk.class)
@Entity
public class UserDetails {
@Id
private String name;

@Id
private String address;

}

public class UserDetailsCK implements Serializable {
	private String name;
	private string address;
	
	//no-args constructor 
	public UserDetailsCk() {
	
	}
	
	@Override 
	public boolean equals (Object obj) {
		if (this == obj) return true;
		if (!(obj instance UserDetailsCK )) {
			return false;
		}
		// downcasting
		UserDetailsCK userck = (UserDeailsCK) obj
		return this.name.equals(userCk.name) && this.name.equals(userCk.address);
	}
	
	@Override
	public int hashCode() {
		return Objects.hash(name, address);
	}
}

9. @GeneratedValue annotation is used to define how primary key would be generated.
9. GenerationType
	1. IDENTITY : @GeneratedValue(strategy = GenerationType.IDENTITY)
		- Each insert generate a new identifier (auto-increment field)
		- It is very DB specific operation, for each time it has to connect with DB to generate next value.
	2. SEQUENCE : 
		- more control then identity as  we can configure start, increment, cached -allocation size of sequence values(from Db we generate from sequence and cache in System that would save from Db hit).
		- Speed up the efficiency when we cache sequece values.
		- @SequenceGenerator(name= "unique_user_seq", sequenceName ="db_seq_name", intitalValue = 100, allocationSize = 5)
		- name, sequenceName: name createded in DB, intitalValue, allocationSize

10. Advantage of Sequence : 
	- custom logic (start, incrementby , maxvalue)
	- Create Sequence user-seq Increment by 25 START WITH 100 MAXVALUE 999
	- Sequence generaation logic is independent of cache
	- Range of Ids can be cached, so we can avoid hitting database each time a new id comes.
	- Better portability, means IDENTIY is very DB specific while Sequence can provide consistent behavioor across multiple DB

11. GenerationType Table

	- @TableGenerator Annotation ise used but its very less efficent 
	- Because seprate table is created, just for managin unique IDs.
	- Each time id is required, Select-Update query is executed.
	- complex concurretly handling, when multiple oerations happing in paralled, It reuired loack and unloack. which leads performance bottlenack.
---------------------------------------------------------------------------------------------	
# Part 5 

1. Relationship Types
	- @OneToOne(cascade={CASCADETYPE.ALL})
	- private UserDetails userDetails 
	- Based on above it auto create forign key with name user_details
	- forign key would be contained on UserDetails side

2. Throw this we can better control forign-key name 
	- @JoinColumn(name="user_address", refrencedColumnName = "id")

3. CascadeType
	- PERSIST : on insert operation of perent, apply insert on child as well.
	- MERGE - When we apply update operation on parent it will aply update in child as well, without it child would not be updated
	- REMOVE - When parent entity row delete/remove child also removed.
	- REFRESH - BYPASS the first level cache and directly retrive data from db
	- DETACH - it will avoid enity to manged by persistent context 
	- ALL - All cascade types affect at ones.
	
4. FeatchType : Like on get operation how/when child enity gets loaded
	- Eager : @OneToOne, @ManyToOne
	- Lazy : @ManyToMany, @OneToMany
	- Manualy mention @OneToOne(cascade={CASCADETYPE.ALL}, fetch= FetchType.LAZY)

Reason : JAKSON Serialization error comes when UserAddress lazyly loaded
Solution : 5,6
5. @jsonIgnore : This will remove the UserAddress field totally for both Lazy and Eager loading.

6. DTO
• Using DTO (Data Transfer Object)
• Much clean and recommended approach.
• Instead of sending Entity directly, first r

7. @OneToOne Bidreational
	- Both entity holds the reference to each other means:
	- UserDetails has reference to UserAddress 
	- Ans UserAddress has a reference back to UserDetails(Only in object, not in actual table)
	- Owner and Inverse side
	- @OneToOne(mappedBy = "userAddress", Featch= FeatchType.EAGER)
	- Left Join Query will be executed UserAddress LEFTJOIN UserDetails.
8. @JsonManagedReference @JsonBackReference
	Why because :
	During response construction:
	1. Jackson starts serializing UserAddress after UserAddress is
	serialized.
	2. It encounters UserDetails within UserAddress and starts
	serializing it.
	After UserDetails is serialized.
	3. Inside UserDetails , it encounters UserAddress again and
	serialization keeps going on in loop.

Infinite Recursion issue in bidirectional mapping can be solved via:

	@JsonManagedReference:
	• Should be Used only in Owing entity.
	• Tells explicitly Jackson to go ahead and serialize the child entity.
	@JsonBackReferenc
	• e: Should only be Used with Inverse/Child entity.
	• Tells explicitly Jackson to not serialize the parent entity.



9. Is there a way that, I can load the associated entity from both side, but still avoid infinite recursion:
	@JsonIdentityInfo
	• During serialization , Jackson gives the unique ID to the entity (based on property
	field).
	• Though which Jackson can know, if that particular id entity is already serialized
	before, then it skip the serialization.
		

-------------------------------------------------------------------------------------------------
# Part 6


1. One To Many
	- Child holds the forign key
	- LazyLoading
	- Join Query runs
	- if we don't define @JoinQuery then it will create an extra table to hold the mappings
	- So here througth @JoinQuery we will tell exactly to create FK in child table.
2. CascadeType.ALL => 
3. OrphanRemoval ->
	- Automatically remove child entry when child removed from parent collection.
	- If we would remove the child element from parent collection. then apply save method then in that it just update the child fk to null.
	- @OneToMany(cascade ="{CascadeType.ALL}", orphanRemoval=false);
	- CacadeRemove vs OrphanRemoval
4. DTO -> Manual calls we don't need to do that because of serialization Jakson will automatically call the child if it was in Lazy Loading condition.
5. Bidirectional oneToMany: mappedBy we mention so that on JavaObject level it store the orderDetaials as well.
6. ManyToMany() : 
	- External table is created created for storing the details of Order and Product in Order_product table.
7. Bidirectional ManyToMany : mappedBy used here.

------------------------------------------------------------------------------------------------
# Part 7 - JPQL, Derived Query, N+1 Problem, Joins, Pagination and Sorting

	- Query(Select new com.dto.UserDTO(ud.name, ad.country) From UserDetails ud Join ud.userAddress as where ud.name = :userFirstName)
	- JOIN Query must see 

1. Derived Query and DerivedMethod
	- There is specific syntex we would create Derived Method based on the it will generate the query.
	- ^(find|read|get|query|search|stream|count|exists|delete|remove)((\\p{Lu}.*?))??By"
	 and camel case annotation by 
	- Automatically generates queries from the methods.
	- Need to follow a specific naming convention.
	- Derived query used for GET/REMOVE operations but not for INSERT/UPDATE
	- Insert and Update operations is supported though "save()"
	- Queries which are little complex and can't be handled via Derived Query, we can
use:
2. Pageble and Sort
	- Paginations and Sorting in Derived Query:
	- JPA provides 2 interfaces to support Pagination and Sorting i.e.
	- Pageable (org.springframework.data.domain) 1. pageNumber 2. pageSize (no of records per page)
	- Sort
	- Sort.by accepts multiple fields.
	- When multiple fields provided, sorting applied in order.
	- first it sort by first field and if there are duplicates then second field is used and
	so on.
3. JPQL OR HPQL Language
	- Database agnostic
	- Enity based language that means 
	- No need to place ON clause in JPQL query as in entity relation is alredy defined.
	- @Query
	- Java Persistence Query Language.
	- Similar to SQL but works on Entity Object instead of direct database.
	- Its database independent
	- Works with Entity name and fields and not with table column names.
	- If we don’t, want Object[] to be used, we can also return direct custom
DTO.
	- Query(Select new com.dto.UserDTO(ud.name, ad.country) From UserDetails ud Join ud.userAddress as where ud.name = :userFirstName)
	- JOIN Query must see 

4. N+1 problem
Problem :
	Say, 1 User can have Many Addresses.
	And our Query is such that, it can fetch more than 1 Users. Then this problem can
	occurs.
	So, say we have 'N' Users. Then below queries will be hit by JPA:
		- 1 query to fetch all the USERS.
		- For each User it will fetch ADDRESSES, so for N users, it will fetch N times.
		- So total number of query hit : N+1.
		So we need to find the way, so that only 1 QUERY it hit instead of N+1.
	- Before going for the solution for this problem, One question might be coming to our
	mind:
	- What if, we use EAGER initialization, then can we avoid this issue?
	- NO because EAGER initialization do not work, when our query tries to fetch multiple
	PARENT rows and that also have multiple CHILD.
	- In previous video, we tested EAGER with "findByID(id)" method, in which it make sure
	that, our query is fetching only 1 PARENT and that can have many CHILD, that’s fine. In
	that JPA internally draft a JOIN query.
	- But when Multiple parent with Multiple child get involved, EAGER do not work in just 1
	query, it first fetches all the parent and then for each parent, it fetch all its child.
	
	- JPA does this optimization for letting complexity low and maintaining consiteny but by apply below scenrious we would explicitly tell JPA to send data via just 1 Query we would handle it. 

Solutions	
	- Join Fetch 
	- @BatchSize(size=10) It wont make only 1 query, but it will reduce it, as it will divide it into
batches
	- @EntityGraph(attributePaths="userAddressList")
		• Used over method (helpful in derived methods)
		• Tell JPA to fetch all the entries of UserAddress along with user details.
5. How to join Many tables?
	- @Query("SELECT a FROM A a JOIN a.bList b JOIN b.cList c WHERE c.someProperty =
:someValue")
List<A> findAWithBAndC(@Param("someValue") String someValue);

6. @Modifying Annotation
	• when @Query annotation used, by-default JPA expects SELECT
	query.
	• If we try to use "DELETE" or "INSERT" or "UPDATE" query with
	@Query, JPA will throw error, that:
	
	- @Modifying annotation, is to tell JPA that, expect either "DELETE" or
"INSERT" or "UPDATE" query with @Query
	• Since we are trying to update the DB, we also need to use @Transactional
annotation.

7. Flush and Clear

	Understanding Usage of Flush and Clear:
	• As we know, Flush just pushed the persistence context changes
	to DB but hold the value in persistence context.
	• Clear, purge the persistence context, and required fresh DB call.
	- Generally used with @Modifying as by using this only we are able to perform manuplating operations
	- Example ;
@Modifying(flushAutomatically= true, clearAutomatically= true)
@Query("Delete From UserDetails ud Where ud.name= :userFirstName")
void deleteByUserName(@Param("userFirstName") String userName);

- namedParameter :varible

8. Pagination and sorting in JPQL as is

	- Pageable page = PageRequest.of(`pageNumber` 1, `PageSize`5)
	- @Query("Select ud From UserDetails ud Where ud.name= :userFirstName")
	void findByUserName(@Param("userFirstName") String userName, page);
	
9. @NamedQuery Annotation 
	- We can name our query so that we can reuse it.
	@Table(name="user_details")
	@Entity
	@NamedQuery(name= "findByUserName", 
		query = Select u from UserDetails u Where u.name = :userFirstName
		)
	public class USerDetails

	- @Query(name= "findByUserName")

----------------------------------------------------------------------------------------------
# Part-8 NativeQuery and criteria API

1. NativeQuery over JPQL :
2. Dynamic NativeQuery : Based on the data we can create Dynamic by using entityManager, StringBuilder: used to build the query and enitityManager.execute(query).
3. Criteria API : We know JPQL is benifited in the situation where we wanted to make a db-agnostic application, but we can not create dynamic JPQL query directly so for that we have CriteriaBuilder cb  = entityManager.getCriteriaBuilder();

CriterialQuery<USerDetails> crQuery = cb.createQuery(UserDetails.class)// return List<UserDetails>

user = crQuery.from(UserDetails.class);
crQuery.select(user);

Prdicate predicate = cb.equals(user.get("phone"), phoneNo);
crQuery.where(predicate1);

TypedQuery<UserDeatils> query = entityManager.createQuery(crQuery);
List<USerDetails> ud = query.getResultList();


# Part - 9

1. Specification API -> Remove duplicate code and boilerplate code from criteria API, which make dynamic JPQL Query writting becomes much easier.
-------------------------------------------------------------------------------------------------

# Part-10 Facts

- In hibernate if you are performing any enity-manipulation operation like firstly findBy() operation and then change that entity,By using @Transactional you do not need to use save() method explicitly as that Model/Entity data is already stored in the persistent-context , so at the end it will flush that data to db and it gets saved.  

Prevention : Use Deatch operation cascadeType for making entity deatach from persistent-context.

These concepts — dirty checking, first-level cache, write-behind, cascading, lazy loading, etc. — all work together to achieve this.

##DIRTY-CHECKING##
In Hibernate (or JPA in general), when you fetch an entity (e.g., using findById, find(), or a custom query), the returned entity is managed, meaning it is attached to the persistence context.

If your method is annotated with @Transactional, you are working inside a transaction.

When you modify fields of a managed entity, you do not need to explicitly call save() (or entityManager.merge()). The changes are automatically detected and synchronized with the database when:

The transaction commits, or

The persistence context is flushed manually (via flush()), whichever comes first.

This is called dirty checking. Hibernate automatically detects the changes and issues an SQL UPDATE as needed.

---------------------------------------------------------------------------------------------------
