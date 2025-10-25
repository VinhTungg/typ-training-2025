# Tài Liệu Học Tập - Backend Web Development

## Mục Lục
- [Phần 1: Database (CSDL Quan Hệ)](#phần-1-database-csdl-quan-hệ)
  - [Cài đặt DBMS](#cài-đặt-dbms)
  - [Các câu lệnh cơ bản với SQL](#các-câu-lệnh-cơ-bản-với-sql)
- [Phần 2: OOP](#phần-2-oop)
  - [OOP trong Java](#oop-trong-java)
  - [Dependency Injection và Inversion of Control](#dependency-injection-và-inversion-of-control)

---

## Phần 1: Database (CSDL Quan Hệ)

### Cài đặt DBMS

Có thể cài đặt một trong các hệ quản trị CSDL sau:
- **MySQL**
- **SQL Server**

#### Các phương thức cài đặt:
- **Online**: Supabase, Cloud Database Services
- **Local**:
  - MySQL Workbench
  - XAMPP
  - AMPPS
  - Docker Container

### Thực hành tạo CSDL

Sau khi cài đặt, tạo một CSDL cho một bài toán thực tế để thực hành:
- Quản lý giải đấu
- Quản lý thư viện
- Quản lý sinh viên
- Quản lý cửa hàng

### Các câu lệnh cơ bản với SQL

#### 1. Thao tác Dữ liệu (DML - Data Manipulation Language)

| Lệnh | Mô tả |
|------|-------|
| `SELECT` | Truy vấn dữ liệu từ bảng |
| `INSERT` | Thêm dữ liệu mới vào bảng |
| `UPDATE` | Cập nhật dữ liệu trong bảng |
| `DELETE` | Xóa dữ liệu khỏi bảng |

**Ví dụ:**
```sql
-- SELECT
SELECT * FROM users WHERE age > 18;

-- INSERT
INSERT INTO users (name, email, age) VALUES ('Nguyen Van A', 'a@email.com', 25);

-- UPDATE
UPDATE users SET age = 26 WHERE id = 1;

-- DELETE
DELETE FROM users WHERE id = 1;
```

#### 2. Định nghĩa Dữ liệu (DDL - Data Definition Language)

| Lệnh | Mô tả |
|------|-------|
| `CREATE TABLE` | Tạo bảng mới |
| `DROP TABLE` | Xóa bảng |
| `ALTER TABLE` | Thay đổi cấu trúc bảng |
| `CREATE VIEW` | Tạo view (tham khảo thêm) |
| `DROP VIEW` | Xóa view (tham khảo thêm) |

**Ví dụ:**
```sql
-- CREATE TABLE
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ALTER TABLE
ALTER TABLE users ADD COLUMN phone VARCHAR(15);

-- DROP TABLE
DROP TABLE users;

-- CREATE VIEW
CREATE VIEW active_users AS
SELECT * FROM users WHERE status = 'active';
```

#### 3. Trigger, Transaction, Procedure, Function

| Lệnh | Mô tả |
|------|-------|
| `CREATE PROCEDURE` | Tạo stored procedure |
| `CREATE FUNCTION` | Tạo hàm |
| `CREATE TRIGGER` | Tạo trigger |
| `COMMIT` | Xác nhận transaction |
| `ROLLBACK` | Hoàn tác transaction |
| `SAVE TRANSACTION` | Lưu điểm trong transaction |

**Ví dụ:**
```sql
-- CREATE PROCEDURE
DELIMITER //
CREATE PROCEDURE GetUsersByAge(IN min_age INT)
BEGIN
    SELECT * FROM users WHERE age >= min_age;
END //
DELIMITER ;

-- CREATE FUNCTION
DELIMITER //
CREATE FUNCTION CalculateAge(birth_date DATE)
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN YEAR(CURDATE()) - YEAR(birth_date);
END //
DELIMITER ;

-- CREATE TRIGGER
DELIMITER //
CREATE TRIGGER before_user_insert
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
    SET NEW.created_at = NOW();
END //
DELIMITER ;

-- TRANSACTION
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- ROLLBACK
START TRANSACTION;
DELETE FROM users WHERE id = 1;
ROLLBACK; -- Hoàn tác thao tác xóa
```

#### 4. Điều khiển Truy cập (DCL - Data Control Language)

| Lệnh | Mô tả |
|------|-------|
| `GRANT` | Cấp quyền cho user |
| `REVOKE` | Thu hồi quyền của user |

**Ví dụ:**
```sql
-- GRANT
GRANT SELECT, INSERT ON database_name.* TO 'username'@'localhost';

-- REVOKE
REVOKE INSERT ON database_name.* FROM 'username'@'localhost';
```

#### 5. Toán tử và Mệnh đề Truy vấn

| Toán tử/Mệnh đề | Mô tả |
|-----------------|-------|
| `FROM` | Chỉ định bảng nguồn |
| `WHERE` | Điều kiện lọc |
| `ORDER BY` | Sắp xếp kết quả |
| `GROUP BY` | Nhóm dữ liệu |
| `HAVING` | Điều kiện cho nhóm |
| `AND` | Toán tử logic AND |
| `OR` | Toán tử logic OR |
| `LIKE` | So khớp mẫu |
| `IN` | Kiểm tra giá trị trong danh sách |
| `BETWEEN` | Kiểm tra giá trị trong khoảng |
| `JOIN` | Kết nối các bảng |

**Ví dụ:**
```sql
-- Truy vấn phức tạp
SELECT 
    u.name, 
    COUNT(o.id) as total_orders,
    SUM(o.amount) as total_amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.age >= 18
    AND u.status = 'active'
    AND o.created_at BETWEEN '2025-01-01' AND '2025-12-31'
GROUP BY u.id, u.name
HAVING total_orders > 5
ORDER BY total_amount DESC
LIMIT 10;
```

### Tài liệu tham khảo
📚 [Tài liệu SQL chi tiết](https://drive.google.com/file/d/1bELh_saWyDgXJ7woWjFEu60I_beb4VQ1/view?usp=sharing)

---

## Phần 2: OOP

### OOP trong Java

#### Java Cơ Bản

##### 1. Object và Class

```java
// Định nghĩa Class
public class Student {
    // Thuộc tính (attributes)
    private String name;
    private int age;
    private String studentId;
    
    // Constructor
    public Student(String name, int age, String studentId) {
        this.name = name;
        this.age = age;
        this.studentId = studentId;
    }
    
    // Phương thức (methods)
    public void study() {
        System.out.println(name + " is studying");
    }
    
    // Getter và Setter
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
}

// Tạo Object
Student student1 = new Student("Nguyen Van A", 20, "SV001");
student1.study();
```

##### 2. Abstract Class

```java
// Abstract Class
public abstract class Animal {
    protected String name;
    
    public Animal(String name) {
        this.name = name;
    }
    
    // Abstract method
    public abstract void makeSound();
    
    // Concrete method
    public void sleep() {
        System.out.println(name + " is sleeping");
    }
}

// Kế thừa Abstract Class
public class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }
    
    @Override
    public void makeSound() {
        System.out.println("Woof! Woof!");
    }
}
```

##### 3. Interface

```java
// Interface
public interface Drawable {
    void draw();
    void resize(int width, int height);
}

public interface Movable {
    void move(int x, int y);
}

// Implement Interface
public class Circle implements Drawable, Movable {
    private int x, y, radius;
    
    @Override
    public void draw() {
        System.out.println("Drawing circle at (" + x + ", " + y + ")");
    }
    
    @Override
    public void resize(int width, int height) {
        this.radius = width / 2;
    }
    
    @Override
    public void move(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
```

##### 4. Biến và Hàm

```java
public class Example {
    // Biến instance
    private int instanceVar;
    
    // Biến static
    private static int staticVar;
    
    // Biến final (hằng số)
    private static final int CONSTANT = 100;
    
    // Hàm instance
    public void instanceMethod() {
        System.out.println("Instance method");
    }
    
    // Hàm static
    public static void staticMethod() {
        System.out.println("Static method");
    }
}
```

##### 5. Input/Output (I/O)

```java
import java.util.Scanner;
import java.io.*;

public class IOExample {
    // Console Input
    public static void readInput() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name);
        scanner.close();
    }
    
    // File Input
    public static void readFile(String filename) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(filename));
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
        reader.close();
    }
    
    // File Output
    public static void writeFile(String filename, String content) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(filename));
        writer.write(content);
        writer.close();
    }
}
```

##### 6. Vòng lặp

```java
public class LoopExamples {
    public static void main(String[] args) {
        // For loop
        for (int i = 0; i < 5; i++) {
            System.out.println("Count: " + i);
        }
        
        // While loop
        int j = 0;
        while (j < 5) {
            System.out.println("Count: " + j);
            j++;
        }
        
        // Do-while loop
        int k = 0;
        do {
            System.out.println("Count: " + k);
            k++;
        } while (k < 5);
        
        // Enhanced for loop (for-each)
        int[] numbers = {1, 2, 3, 4, 5};
        for (int num : numbers) {
            System.out.println("Number: " + num);
        }
    }
}
```

### Các Tính Chất OOP

#### 1. Encapsulation (Đóng gói)
Ẩn giấu thông tin và chỉ cho phép truy cập thông qua các phương thức công khai.

```java
public class BankAccount {
    private double balance; // Thuộc tính private
    
    public BankAccount(double initialBalance) {
        if (initialBalance > 0) {
            this.balance = initialBalance;
        }
    }
    
    // Public methods để truy cập và thay đổi balance
    public double getBalance() {
        return balance;
    }
    
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }
    
    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }
}
```

#### 2. Inheritance (Kế thừa)
Cho phép class con kế thừa các thuộc tính và phương thức từ class cha.

```java
// Class cha
public class Vehicle {
    protected String brand;
    protected int year;
    
    public Vehicle(String brand, int year) {
        this.brand = brand;
        this.year = year;
    }
    
    public void start() {
        System.out.println("Vehicle is starting");
    }
}

// Class con kế thừa
public class Car extends Vehicle {
    private int numberOfDoors;
    
    public Car(String brand, int year, int numberOfDoors) {
        super(brand, year); // Gọi constructor của class cha
        this.numberOfDoors = numberOfDoors;
    }
    
    @Override
    public void start() {
        System.out.println("Car is starting with " + numberOfDoors + " doors");
    }
}
```

#### 3. Polymorphism (Đa hình)
Một đối tượng có thể có nhiều hình thái khác nhau.

```java
public class Shape {
    public double calculateArea() {
        return 0;
    }
}

public class Rectangle extends Shape {
    private double width, height;
    
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
    
    @Override
    public double calculateArea() {
        return width * height;
    }
}

public class Circle extends Shape {
    private double radius;
    
    public Circle(double radius) {
        this.radius = radius;
    }
    
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
}

// Sử dụng Polymorphism
public class Main {
    public static void main(String[] args) {
        Shape shape1 = new Rectangle(5, 10);
        Shape shape2 = new Circle(7);
        
        System.out.println("Rectangle area: " + shape1.calculateArea());
        System.out.println("Circle area: " + shape2.calculateArea());
    }
}
```

#### 4. Abstraction (Trừu tượng)
Ẩn đi các chi tiết triển khai và chỉ hiển thị các tính năng cần thiết.

```java
public abstract class PaymentMethod {
    protected double amount;
    
    public PaymentMethod(double amount) {
        this.amount = amount;
    }
    
    // Abstract method
    public abstract boolean processPayment();
    
    // Concrete method
    public void printReceipt() {
        System.out.println("Payment of " + amount + " processed successfully");
    }
}

public class CreditCardPayment extends PaymentMethod {
    private String cardNumber;
    
    public CreditCardPayment(double amount, String cardNumber) {
        super(amount);
        this.cardNumber = cardNumber;
    }
    
    @Override
    public boolean processPayment() {
        // Logic xử lý thanh toán qua thẻ tín dụng
        System.out.println("Processing credit card payment...");
        return true;
    }
}
```

### Tài liệu tham khảo
📚 [Tài liệu Java OOP chi tiết](https://drive.google.com/file/d/11hmx-23wpZh6bn2VFfi5t7eU8JfnM952/view?usp=sharing)

---

## Dependency Injection và Inversion of Control

### 1. Dependency Injection (DI)

#### Khái niệm
Dependency Injection là một design pattern cho phép việc tạo ra các dependencies của một object từ bên ngoài, thay vì object tự tạo ra chúng.

#### Lợi ích:
- Giảm sự phụ thuộc giữa các class
- Dễ dàng testing
- Code dễ bảo trì và mở rộng
- Tăng tính linh hoạt

#### Ví dụ không sử dụng DI:
```java
public class UserService {
    private UserRepository repository;
    
    public UserService() {
        // Tự tạo dependency - Tight coupling
        this.repository = new UserRepository();
    }
    
    public User getUser(int id) {
        return repository.findById(id);
    }
}
```

#### Ví dụ sử dụng DI:

##### a) Constructor Injection (Khuyến khích)
```java
public class UserService {
    private final UserRepository repository;
    
    // Dependency được inject qua constructor
    public UserService(UserRepository repository) {
        this.repository = repository;
    }
    
    public User getUser(int id) {
        return repository.findById(id);
    }
}

// Sử dụng
UserRepository repository = new UserRepository();
UserService service = new UserService(repository);
```

##### b) Setter Injection
```java
public class UserService {
    private UserRepository repository;
    
    // Dependency được inject qua setter
    public void setRepository(UserRepository repository) {
        this.repository = repository;
    }
    
    public User getUser(int id) {
        return repository.findById(id);
    }
}
```

##### c) Interface Injection
```java
public interface RepositoryInjector {
    void injectRepository(UserRepository repository);
}

public class UserService implements RepositoryInjector {
    private UserRepository repository;
    
    @Override
    public void injectRepository(UserRepository repository) {
        this.repository = repository;
    }
}
```

### 2. Inversion of Control (IoC)

#### Khái niệm
Inversion of Control là một nguyên lý thiết kế trong đó việc điều khiển luồng chương trình được đảo ngược. Thay vì chương trình tự điều khiển việc tạo và quản lý các dependencies, một framework hoặc container sẽ đảm nhiệm việc này.

#### IoC Container
```java
// IoC Container đơn giản
public class SimpleIoCContainer {
    private Map<Class<?>, Object> instances = new HashMap<>();
    
    public <T> void register(Class<T> type, T instance) {
        instances.put(type, instance);
    }
    
    @SuppressWarnings("unchecked")
    public <T> T resolve(Class<T> type) {
        return (T) instances.get(type);
    }
}

// Sử dụng IoC Container
public class Main {
    public static void main(String[] args) {
        SimpleIoCContainer container = new SimpleIoCContainer();
        
        // Đăng ký dependencies
        UserRepository repository = new UserRepository();
        container.register(UserRepository.class, repository);
        
        // Resolve dependency
        UserRepository resolvedRepo = container.resolve(UserRepository.class);
        UserService service = new UserService(resolvedRepo);
    }
}
```

### 3. DI/IoC trong Spring Framework

#### Ví dụ với Spring Boot:

```java
// Repository
@Repository
public class UserRepository {
    public User findById(Long id) {
        // Logic truy vấn database
        return new User();
    }
}

// Service với Constructor Injection
@Service
public class UserService {
    private final UserRepository userRepository;
    
    // Spring tự động inject UserRepository
    @Autowired
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    
    public User getUser(Long id) {
        return userRepository.findById(id);
    }
}

// Controller
@RestController
@RequestMapping("/api/users")
public class UserController {
    private final UserService userService;
    
    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    @GetMapping("/{id}")
    public User getUser(@PathVariable Long id) {
        return userService.getUser(id);
    }
}
```

#### Configuration với Spring:

```java
@Configuration
public class AppConfig {
    
    @Bean
    public UserRepository userRepository() {
        return new UserRepository();
    }
    
    @Bean
    public UserService userService(UserRepository repository) {
        return new UserService(repository);
    }
}
```

### 4. Ví dụ DI/IoC trong C#

```csharp
// Interface
public interface IUserRepository {
    User GetById(int id);
}

// Implementation
public class UserRepository : IUserRepository {
    public User GetById(int id) {
        // Logic truy vấn database
        return new User();
    }
}

// Service
public class UserService {
    private readonly IUserRepository _repository;
    
    // Constructor Injection
    public UserService(IUserRepository repository) {
        _repository = repository;
    }
    
    public User GetUser(int id) {
        return _repository.GetById(id);
    }
}

// Đăng ký DI trong ASP.NET Core (Program.cs)
var builder = WebApplication.CreateBuilder(args);

// Đăng ký services
builder.Services.AddScoped<IUserRepository, UserRepository>();
builder.Services.AddScoped<UserService>();

var app = builder.Build();
```

### Tổng kết DI/IoC

| Khái niệm | Mô tả |
|-----------|-------|
| **DI** | Kỹ thuật inject dependencies từ bên ngoài |
| **IoC** | Nguyên lý đảo ngược quyền điều khiển |
| **IoC Container** | Framework quản lý việc tạo và inject dependencies |

#### Lợi ích chính:
1. ✅ Giảm coupling giữa các components
2. ✅ Dễ dàng unit testing (có thể mock dependencies)
3. ✅ Code dễ maintain và mở rộng
4. ✅ Tái sử dụng code tốt hơn
5. ✅ Tuân thủ SOLID principles

---

## Ghi chú

- 📝 Thực hành thường xuyên với các bài tập cụ thể
- 💡 Tham khảo tài liệu chính thức của Java, MySQL, Spring Framework
- 🚀 Bắt đầu với các project nhỏ để áp dụng kiến thức
- 📚 Đọc source code của các open-source projects để học hỏi

---

**Cập nhật lần cuối:** October 25, 2025

