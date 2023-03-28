> 像自然语言一样阅读编程语言

## 预备概念


1. 设，一般用来构造未知数、变量、函数、向量等。是一种为便于表达而构建数学符号时所采用的语言。
2. 令，一般表示在论证、解释、解题，过程中，满足题设（题目要求）的情况下，所设变量必须满足的关系（如相等、互为相反数、互为倒数等）。是一种用于描述解题过程的语言。

特殊的，如果题目中已经给出的变量关系式，为了便于描述、论证而再给予设改的，应用“令”。（如：已知，y=x。为了方便，可令F(x)=x。



## 关键字词典


1. let，数学（设，令），让，为，把，设置，使。假设，让；允许；由；准许。
2. mut，可变的
3. const 常数
4. `->` 细箭头表示返回
5. 当用 ! 作函数返回类型的时候，表示该函数永不返回( diverge function )发散函数
6. Trait，意思为特征
7. println！换行输出
8. &，获取变量的引用，称之为借用(borrowing)
9. `..` 意思为 range 序列语法
10. `_` 代表匹配一个值，在 Rust 中 _ 的含义是忽略该值或者类型的意思
11. array 为数组
12. Vector 为动态数组
13. 切片类型：`[T]`
14. 切片引用类型：`&[T]`   例如 `&[i32]`
15. 元组成员，类型签名
16. 11. A.B则A为对象或者结构体；点号（.）：左边必须为实体。


1. `::`是作用域运算符，
    1.  `A::B`表示作用域A中的-名称B，A可以是名字空间、类、结构；
    2.  我们通过 `::` 操作符来访问 PokerSuit 下的具体成员





### 方法组与概念组

1. 字符串
   1. 字符串可以看成栈模型，最后一个字符为栈顶。
   2. 可变字符串 String
   3. 不变字符串 &str（字符串切片），

可变字符串方法：pop，来自栈操作弹出。push，来自栈操作，追加。


## 自然语序阅读

### 所有权

> 所有者 = 从属对象，，赋值为，绑定为。
> 将数值 5 绑定到 x


```rust
let x = 5;  //令 x 绑定5
let y = &x;  //令 y 绑定 借用的x
assert_eq!(5, x);
assert_eq!(5, *y);  //断言相等 5，解引用y
```

```rust
let a = "hello world"，令 a 绑定为 hello world
let mut x = 5; 令 可变的 x 绑定为 5。
var a = "hello world"， a 赋值为 hello world。
x = 6;，x 修改为 6
let (a, mut b): (bool,bool) = (true, false);，令  元组a可变的b，类型是 布尔，布尔，匹配被绑定元组值真，假。
```


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



可变引用需要使所有者修饰为可变的。同一作用域，特定数据只能有一个可变引用：


`fn greet(name: String)，方法 green 参数name类型（冒号说明） string`

```rust
let s = String::from("hello world");
let hello = &s[0..5];  // 令 hello 绑定为 借用s 切片0至5部分序列。


let s3 = s1 + &s2;，令 s3 绑定为 转移（所有权）s1 加 借用 s2，其中s1，s2为string可变类型。

let (s2, len) = calculate_length(s1);，令 元组 s2 len 绑定 calculate_length函数接管s1后的返回值。
```


**takes_ownership(s); 调用函数并移动（无copy特性，移动到函数中。）或Copy s 的值到函数里。如果一个类型拥有 Copy 特征，一个旧的变量在被赋值给其他变量后仍然可用。**

> 实现了 Copy 特征的类型无需所有权转移，可以直接在赋值时进行 数据拷贝



### 结构体

> 结构体，元组结构体，单元结构体（仅有结构体 名称）

一个结构体由几部分组成:

1. 通过关键字 struct 定义
2. 一个清晰明确的结构体 名称
3. 几个有名字的结构体 字段

```rust
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
```

**设 结构 User，其中 active 字段类型为 布尔，username类型为String。。。**

```rust
let user1 = User {
    email: String::from("someone@example.com"),
```

**令 user1 绑定 User 结构体，其中，email字段值为String::from("someone@example.com"),。。**

```rust
let user2 = User {
    email: String::from("another@example.com"),
    ..user1  //结构体更新语法 ..user1
```

**令 user2 绑定 User结构体，（省略），更新自user1结构体。**



### 枚举

```rust

enum PokerCard {
    Clubs(u8),
    Spades(u8),
    Diamonds(u8),
    Hearts(u8),
}

fn main() {
   let c1 = PokerCard::Spades(5);
   let c2 = PokerCard::Diamonds(13);
}

```

**设 枚举 PokerCard 定义成员，Clubs类型为u8，，，Hearts 类型为u8。**

**设 枚举 PokerCard 定义成员 xx，xx。**

**令 c1 绑定 PokerCard枚举中的Spades成员，关联 5**


### 定长数组和不定长数组

```rust
let a = [1, 2, 3, 4, 5];

令 a 绑定 数组[1, 2, 3, 4, 5];

let a: [i32; 5] = [1, 2, 3, 4, 5];

令 a 类型为数组其中元素类型 i32 数组长度5（[类型; 长度]） 绑定 数组[1, 2, 3, 4, 5];

let a = [3; 5]; 令 a 绑定 数组 其值为3，重复5次。（copy特性）
```



### 循环体

> for iterating_var in sequence：对于var元素在集合（序列）中

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


loop 环，环路

break 可以单独使用，也可以带一个返回值，有些类似 return
loop 是一个表达式，因此可以返回一个值


`a.iter().enumerate() A. 迭代(). 列举()`


### 匹配模式

```rust

match target {
    模式1 => 表达式1,
    模式2 => {
        语句1;
        语句2;
        表达式2
    },
    _ => 表达式3
}

```

match 的分支。一个分支有两个部分：一个模式和针对该模式的处理代码


**一次匹配match与多次匹配if let**


**match 中的变量覆盖**其实不是那么的容易看出，要小心。其原因是match块或分支中的同名变量是新变量。

> 变量遮蔽，一个是在同一作用域使用let =  ，另一种是在子作用域使用let =，作用范围仅限该作用域。


把模式（pattern）看作正则表达式就好理解多了。


**匹配的单分支多模式** a | b 或者 1..=5序列。


解构即：已知原有的结构，用含有具体变量的结构解析式表达该结构；也可以使用模式来解构结构体、枚举、元组、数组和引用。这种将复杂类型分解匹配的方式，可以让我们单独得到感兴趣的某个值。


匹配绑定。


**函数调用可以用数学视角视作，a f(a)**

在 Rust 中，解构是一种将复合数据类型（如元组、结构体、枚举等）拆分为其组成部分的方法。解构可以将一个复合数据类型的元素或字段赋值到单独的变量中，这样我们可以更方便地访问和操作数据。
