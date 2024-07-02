联合类型（Union Types）和交叉类型（Intersection Types）是 TypeScript 中的两种类型操作符，它们具有不同的行为和用途。

1. 联合类型（Union Types）：
    - 用竖线 `|` 分隔多个类型，表示一个值可以是其中的任意一种类型之一。
    - 联合类型适用于变量或参数可以接受多种类型的情况。
    - 联合类型使用的是"或"的逻辑关系。
    - 例如，`number | string` 表示一个值可以是数字类型或字符串类型。

```ts
let value: number | string;
value = 10; // 合法
value = "hello"; // 合法
value = true; // 不合法，因为布尔类型不在联合类型中
```

2. 交叉类型（Intersection Types）：
    - 使用 `&` 符号将多个类型组合在一起，表示一个值必须同时具有所有这些类型的特征。
    - 交叉类型适用于需要将多个类型的属性和方法合并成一个类型的情况。
    - 交叉类型使用的是"与"的逻辑关系。
    - 例如，`A & B` 表示一个值必须同时具有类型 A 和类型 B 的属性和方法。

```ts
type Person = {
  name: string;
};

type Employee = {
  employeeId: number;
};

let person: Person & Employee;
person = { name: "John Doe", employeeId: 123 }; // 合法
person = { name: "Jane Smith" }; // 不合法，因为缺少 employeeId 属性
```

总结：

- 联合类型表示一个值可以是多种类型之一。
- 交叉类型表示一个值必须同时具有多个类型的特征。
- 联合类型使用 `|` 分隔类型，交叉类型使用 `&` 分隔类型。
- 联合类型使用"或"的逻辑关系，交叉类型使用"与"的逻辑关系。

根据你的需求和场景，你可以选择使用联合类型或交叉类型来表示不同的类型组合和行为。