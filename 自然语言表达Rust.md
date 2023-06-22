> 像自然语言一样阅读编程语言

## 预备概念


1. 设，一般用来构造未知数、变量、函数、向量等。是一种为便于表达而构建数学符号时所采用的语言。
2. 令，一般表示在论证、解释、解题，过程中，满足题设（题目要求）的情况下，所设变量必须满足的关系（如相等、互为相反数、互为倒数等）。是一种用于描述解题过程的语言。

特殊的，如果题目中已经给出的变量关系式，为了便于描述、论证而再给予设改的，应用“令”。（如：已知，y=x。为了方便，可令F(x)=x。



## 关键字词典


1. let，数学（设，令），让，为，把，设置，使。假设，让；允许；由；准许。
2. mut，可变的
3. const 常数
4. fn 函数
5. `->` 细箭头表示返回
6. 当用 ! 作函数返回类型的时候，表示该函数永不返回( diverge function )发散函数
7. Trait，意思为特征
8. println！换行输出
9. &，获取变量的引用，称之为借用(borrowing)
10. `..` 意思为 range 序列语法
11. `_` 代表匹配一个值，在 Rust 中 _ 的含义是忽略该值或者类型的意思
12. array 为数组
13. Vector 为动态数组
14. 切片类型：`[T]`
15. 切片引用类型（数组切片）：`&[T]`   例如 `&[i32]`
16. 元组成员，类型签名
17. 11. A.B则A为对象或者结构体；点号（.）：左边必须为实体。
18. pub "公开"，公开的或"可访问的"。可见性，可见程度。在 Rust 中，默认情况下所有成员都是私有的。可以通过将成员标记为 `pub` 来公开它们。这是 Rust 中的一项设计决策，旨在促进封装和更安全的代码。
19. impl 实现。
20. break 退出，中断。
21. loop 环路。
22. `::`是作用域运算符，
    1.  `A::B`表示作用域A中的-名称B，A可以是名字空间、类、结构；
    2.  我们通过 `::` 操作符来访问 PokerSuit 下的具体成员
23. match 匹配





### 方法组与概念组

1. 字符串
   1. 字符串可以看成栈模型，最后一个字符为栈顶。
   2. 可变字符串 String
   3. 不变字符串 &str（字符串切片），

可变字符串方法：pop，来自栈操作弹出。push，来自栈操作，追加。


## 自然语序阅读

### 所有权

> **所有者 = 从属对象，，赋值为，绑定为。**
> 
> 将数值 5 绑定到 x


```rust
let x = 5;  //令 x 绑定5
let y = &x;  //令 y 绑定 借用的x
assert_eq!(5, x);
assert_eq!(5, *y);  //断言相等 5，解引用y

let a = "hello world"; //令 a 绑定为 hello world
let mut x = 5; //令 可变的 x 绑定为 5。
x = 6; //x 修改为 6
let (a, mut b): (bool,bool) = (true, false);  //令  元组a可变的b，类型是 布尔，布尔，匹配被绑定元组值真，假。
```

var a = "hello world"， a 赋值为 hello world。





### 解构


> 解构：用同样的形式把一个复杂对象中的值匹配出来。

```rust
let (a, b, c, d, e);，设 元组abcde。
(a, b) = (1, 2);，元组 ab 匹配绑定到 1，2
```

> 解构式赋值

```rust
const MAX_POINTS: u32 = 100_000;，常数 maxpoint类型冒号 u32，声明为100000。

let tup: (i32, f64, u8) = (500, 6.4, 1);，令 tup 类型是元组 (i32, f64, u8)，被绑定元组值 (500, 6.4, 1)，
```

```rust

//用 . 来访问元组，元组的索引从 0 开始。

let x: (i32, f64, u8) = (500, 6.4, 1);
let five_hundred = x.0;
let six_point_four = x.1;
let one = x.2;

```

> 可变引用需要使所有者修饰为可变的。同一作用域，特定数据只能有一个可变引用：


`fn greet(name: String)，方法 green 参数name类型（冒号说明） string`

```rust
let s = String::from("hello world");
let hello = &s[0..5];  // 令 hello 绑定为 借用s 切片0至5部分序列。


let s3 = s1 + &s2;，令 s3 绑定为 转移（所有权）s1 加 借用 s2，其中s1，s2为string可变类型。

let (s2, len) = calculate_length(s1);，令 元组 s2 len 绑定 calculate_length函数接管s1后的返回值。
```


takes_ownership(s); 调用函数并移动（无copy特性，移动到函数中。）或Copy s 的值到函数里。如果一个类型拥有 Copy 特征，一个旧的变量在被赋值给其他变量后仍然可用。

> 实现了 Copy 特征的类型无需所有权转移，可以直接在赋值时进行 数据拷贝



### 结构体

> 结构体，元组结构体，单元结构体（仅有结构体 名称）

一个结构体由几部分组成：通过关键字 `struct 定义`、一个清晰明确的`结构体 名称`、几个有名字的`结构体 字段`

```rust
// 设 结构 User，其中 active 字段类型为 布尔，username类型为String。。。
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```



```rust
// 令 user1 绑定 User 结构体，其中，email字段值为String::from("someone@example.com"),。。
let user1 = User {
    email: String::from("someone@example.com"),
```



```rust
// 令 user2 绑定 User结构体，（省略），更新自user1结构体。
let user2 = User {
    email: String::from("another@example.com"),
    ..user1  //结构体更新语法 ..user1
```


### 枚举

```rust
// 设 枚举 PokerCard 定义成员，Clubs类型为u8，，，Hearts 类型为u8。
enum PokerCard {
    Clubs(u8),
    Spades(u8),
    Diamonds(u8),
    Hearts(u8),
}

fn main() {
    // 令 c1 绑定 PokerCard枚举的Spades成员，关联 5
   let c1 = PokerCard::Spades(5);
   let c2 = PokerCard::Diamonds(13);
}

```


### 定长数组和不定长数组

```rust
// 令 a 绑定 数组[1, 2, 3, 4, 5];
let a = [1, 2, 3, 4, 5];


// 令 a 类型为数组其中元素类型 i32 数组长度5（[类型; 长度]） 绑定 数组[1, 2, 3, 4, 5];
let a: [i32; 5] = [1, 2, 3, 4, 5];


// 令 a 绑定 数组 其值为3，重复5次。（copy特性）
let a = [3; 5]; 
```



### 循环体

> for iterating_var in sequence：对于var元素在集合（序列）中
>
> loop 环，环路;  
> loop 是一个表达式，因此可以返回一个值.
> 
> break 可以单独使用，也可以带一个返回值，有些类似 return


```rust
// A.迭代().列举()
a.iter().enumerate() 
```

```rust
for i in 1..=5 {
// 对于 i 在1至5序列中。
        println!("{}", i);
    }

for item in &container {
  // ...
}
```



> while （condition）当 条件怎样时

```rust
while n <= 5  {
    // 当 n 小于等于 5 时
        println!("{}!", n);
        n = n + 1;
    }
```



### 匹配模式

> 把模式（pattern）看作正则表达式就好理解多了。


1. 一次匹配match
2. 多次匹配if let


```rust

match target {
    // match 的分支。一个分支有两个部分：一个模式和针对该模式的处理代码
    模式1 => 表达式1,
    模式2 => {
        语句1;
        语句2;
        表达式2
    },
    // 单分支多模式：a | b 或者 1..=5序列。
    _ => 表达式3
}

```

匹配绑定。

####  match 中的变量覆盖


match 中的变量覆盖其实不是那么的容易看出，要小心。其原因是match块或分支中的同名变量是新变量。

> 变量遮蔽，一个是在同一作用域使用let =  ，另一种是在子作用域使用let =，作用范围仅限该作用域。


**函数调用可以用数学视角视作，a f(a)**


解构即：已知原有的结构，用含有具体变量的结构解析式表达该结构；也可以使用模式来解构结构体、枚举、元组、数组和引用。这种将复杂类型分解匹配的方式，可以让我们单独得到感兴趣的某个值。

在 Rust 中，解构是一种将复合数据类型（如元组、结构体、枚举等）拆分为其组成部分的方法。解构可以将一个复合数据类型的元素或字段赋值到单独的变量中，这样我们可以更方便地访问和操作数据。


```rust
struct Circle {
    x: f64,
    y: f64,
    radius: f64,
}

impl Circle {
    // new是Circle的关联函数，因为它的第一个参数不是self，且new并不是关键字
    // 这种方法往往用于初始化当前结构体的实例
    fn new(x: f64, y: f64, radius: f64) -> Circle {
        Circle {
            x: x,
            y: y,
            radius: radius,
        }
    }

    // Circle的方法，&self表示借用当前的Circle结构体
    fn area(&self) -> f64 {
        std::f64::consts::PI * (self.radius * self.radius)
    }
}

```

impl Rectangle {} 表示为 Rectangle 实现方法(impl 是实现 implementation 的缩写)，这样的写法表明 impl 语句块中的一切都是跟 Rectangle 相关联的。


impl 实现。impl Circle 实现 Circle 结构。

fn new(x: f64, y: f64, radius: f64) -> Circle
方法 new 参数  x 类型 f64，y类型f64，radius类型f64 返回值类型Circle结构。

---

```rust
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}
```

在 area 的签名中，我们使用
-  &self 替代 rectangle: &Rectangle，&self 其实是 self: &Self 的简写（注意大小写）。
- 在一个 impl 块内，Self 指代被实现方法的结构体类型，self 指代此类型的实例，


- 换句话说，self 指代的是 Rectangle 结构体实例，这样的写法会让我们的代码简洁很多，而且非常便于理解：我们为哪个结构体实现方法，那么 self 就是指代哪个结构体的实例。

需要注意的是，self 依然有所有权的概念：

- self 表示 Rectangle 的所有权转移到该方法中，这种形式用的较少
- &self 表示该方法对 Rectangle 的不可变借用
- &mut self 表示可变借用

总之，self 的使用就跟函数参数一样，要严格遵守 Rust 的所有权规则。


&self  
  - rectangle : &Rectangle 
  - self （实例）: &Self （类型）


定义在 impl 中且没有 self 的函数被称之为**关联函数**

---

关联函数与实例方法

关联于某个类型，所以使用这种方式，String::from()
方法：无法独立调用，必须先有类型的实例，再有方法。比如f.read()等。

除了结构体和枚举，我们还能为特征(trait)实现方法

---

泛型：用同一功能的函数处理不同类型的数据，例如两个数的加法，无论是整数还是浮点数，甚至是自定义类型，都能进行支持。

“通用的炮管”就是多态

实际上，泛型就是一种多态。


方法中使用泛型

```rs
impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}
```

```rs
fn display_array<T: std::fmt::Debug, const N: usize>(arr: [T; N]) {
    println!("{:?}", arr);
}
fn main() {
    let arr: [i32; 3] = [1, 2, 3];
    display_array(arr);

    let arr: [i32; 2] = [1, 2];
    display_array(arr);
}
```


泛型约束的后置型

```rs
fn f1<T>(v:T) -> i32
  where T:Add { // 左边就是泛型约束了
  // ...
}

pub enum Assert<const CHECK: bool> {
    //
}
```

---


特征：是一组方法。抽象至不同的类中的相同行为。

```rs
impl Summary for Post {
    fn summarize(&self) -> String {
        format!("文章{}, 作者是{}", self.title, self.author)
    }
}
```

实现特征的语法与为结构体、枚举实现方法很像：impl Summary for Post，读作“为 Post 类型实现 Summary 特征”，然后在 impl 的花括号中实现该特征的具体方法。




```rs
pub trait Summary {
    fn summarize(&self) -> String;
}
```

公开 特征 Summary ，函数 summarize 借用实例 返回值类型 String。


---


函数签名（Function Signature）是指函数的定义或声明中包含的信息，包括函数名、参数列表和返回值类型。函数签名可以用来区分不同的函数，并在调用函数时检查参数类型和数量的正确性。

---

如果你想要为类型 A 实现特征 T，那么 A 或者 T 至少有一个是在当前作用域中定义的！


```rs
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```


实现了Summary特征 的 item 参数。


你可以使用任何实现了 Summary 特征的类型作为该函数的参数，同时在函数体内，还可以调用该特征的方法，例如 summarize 方法。具体的说，可以传递 Post 或 Weibo 的实例来作为参数，而其它类如 String 或者 i32 的类型则不能用做该函数的参数，因为它们没有实现 Summary 特征。



---

"where" 在 Rust 中是一个关键字，用于指定泛型参数的 trait 约束。可以理解为约束（constraint）。

全部,哪里,在哪里,在那里,到哪里,处于哪种情形,地点,…的地方,…情况下,何地,何处,什么地方

在 Rust 中，我们有一个使用 where 子句表示的边界概念。子句适用于任意类型以及类型参数。


----

特征约束不就是约束嘛和泛型约束差不多，只不过换成了特征。

----


dyn是trait对象类型的前缀，dyn 关键字只用在特征对象的类型声明上，在创建时无需使用 dyn。

解引用操作符*，`*self`，Deref Trait

特征对象指向实现了 Draw 特征的类型的实例，也就是指向了 Button 或者 SelectBox 的实例，这种映射关系是存储在一张表中，可以在运行时通过特征对象找到具体调用的类型方法。

可以通过 & 引用或者 Box<T> 智能指针的方式来创建特征对象。

----