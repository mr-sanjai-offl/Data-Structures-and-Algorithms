# 2882. Drop Duplicate Rows

[![LeetCode Link](https://img.shields.io/badge/LeetCode-Problem_Link-FFA116?style=flat-square&logo=leetcode)](https://leetcode.com/problems/drop-duplicate-rows/)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-22c55e?style=flat-square)

## Problem Statement

<pre>
DataFrame customers
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+
</pre>

<p>There are some duplicate rows in the DataFrame based on the <code>email</code> column.</p>

<p>Write a solution to remove these duplicate rows and keep only the <strong>first</strong> occurrence.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<pre>
<strong class="example">Example 1:</strong>
<strong>Input:</strong>
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 5           | Finn    | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
<strong>Output: </strong> 
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
<strong>Explanation:</strong>
Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.
</pre>


---
*Synced automatically with [AlgoVault](https://github.com/mr-sanjai-offl/AlgoVault)*