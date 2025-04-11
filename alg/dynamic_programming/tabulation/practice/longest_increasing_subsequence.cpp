/*
 * ### **💡 Problem: Longest Increasing Subsequence (LIS) – Tabulation**
#### **Problem Statement:**
Given an array **`nums`** of length **`n`**, find the **length of the longest increasing subsequence**.

A **subsequence** is a sequence that appears in the same order but may not be contiguous.

---

### **🔹 Example Input/Output**
#### **Example 1**
📥 **Input:**  
```
nums = [10, 9, 2, 5, 3, 7, 101, 18]
```
📤 **Output:**  
```
4
```
📖 **Explanation:**  
The longest increasing subsequence is **`[2, 3, 7, 18]`**, which has **length = 4**.

#### **Example 2**
📥 **Input:**  
```
nums = [0, 1, 0, 3, 2, 3]
```
📤 **Output:**  
```
4
```
📖 **Explanation:**  
The LIS is **`[0, 1, 2, 3]`**.

#### **Example 3**
📥 **Input:**  
```
nums = [7, 7, 7, 7, 7, 7, 7]
```
📤 **Output:**  
```
1
```
📖 **Explanation:**  
Since all elements are the same, the longest increasing subsequence is just **one element**.

---

### **🔍 Constraints**
- \( 1 \leq \) `nums.length` \( \leq 2500 \) (**Large Input!** 🚀)
- \( -10^4 \leq \) `nums[i]` \( \leq 10^4 \)

---

#### **📝 Your Task**
Think about the following before implementing:
1. **What will the DP table store?**
2. **What is the recurrence relation?**
3. **What will be the base case?**
4. **What order will you fill the table?**
5. **How will you extract the final answer?**

🚀 **Let me know when you're ready for the solution!** 🔥
*/
