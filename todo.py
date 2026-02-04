#!/usr/bin/env python3
"""
待办事项清单 Skill v2.0
增强版任务管理工具（支持优先级和到期日期）
"""

from datetime import datetime

class TodoList:
    """待办事项列表"""

    def __init__(self):
        self.todos = []

    def add(self, task, priority="中", due_date=None):
        """添加任务（带优先级和到期日期）"""
        self.todos.append({
            "task": task,
            "done": False,
            "priority": priority,
            "due_date": due_date,
            "created_at": datetime.now().strftime("%Y-%m-%d")
        })
        due_str = f" (截止: {due_date})" if due_date else ""
        print(f"✅ 已添加任务: {task} [优先级:{priority}]{due_str}")

    def list(self):
        """列出所有任务（显示优先级和到期日期）"""
        if not self.todos:
            print("📝 暂无任务")
            return

        # 按优先级排序：高 > 中 > 低
        priority_order = {"高": 0, "中": 1, "低": 2}
        sorted_todos = sorted(self.todos, key=lambda x: (x["done"], priority_order.get(x["priority"], 1)))

        print("\n📋 待办事项清单:")
        print("-" * 70)
        for i, todo in enumerate(sorted_todos, 1):
            status = "✓" if todo["done"] else " "
            priority = todo.get("priority", "中")
            due = todo.get("due_date", "")
            due_str = f" 📅 {due}" if due else ""

            # 优先级图标
            priority_icon = {"高": "🔴", "中": "🟡", "低": "🟢"}.get(priority, "⚪")

            print(f"{i}. [{status}] {todo['task']} {priority_icon}{due_str}")
        print("-" * 70)

    def complete(self, index):
        """标记任务完成"""
        if 1 <= index <= len(self.todos):
            self.todos[index - 1]["done"] = True
            task = self.todos[index - 1]["task"]
            print(f"🎉 已完成任务: {task}")
        else:
            print("❌ 无效的任务编号")

    def delete(self, index):
        """删除任务"""
        if 1 <= index <= len(self.todos):
            deleted = self.todos.pop(index - 1)
            print(f"🗑️  已删除任务: {deleted['task']}")
        else:
            print("❌ 无效的任务编号")


def main():
    """主程序"""
    todo = TodoList()

    print("=" * 50)
    print("待办事项清单 v2.0".center(50))
    print(" 增强版 - 支持优先级和到期日期 ".center(50))
    print("=" * 50)

    while True:
        print("\n请选择操作:")
        print("1. ➕ 添加任务")
        print("2. 📋 查看任务")
        print("3. ✓ 完成任务")
        print("4. 🗑️  删除任务")
        print("0. 🚪 退出")

        choice = input("\n请输入选项 (0-4): ").strip()

        if choice == '0':
            print("\n再见！")
            break

        elif choice == '1':
            task = input("请输入任务: ").strip()
            if task:
                # v2.0 新增：优先级和到期日期
                priority = input("优先级 (高/中/低，默认中): ").strip() or "中"
                if priority not in ["高", "中", "低"]:
                    priority = "中"
                due_date = input("截止日期 (YYYY-MM-DD，可选): ").strip() or None
                todo.add(task, priority, due_date)

        elif choice == '2':
            todo.list()

        elif choice == '3':
            todo.list()
            if todo.todos:
                index = int(input("\n请输入要完成的任务编号: "))
                todo.complete(index)

        elif choice == '4':
            todo.list()
            if todo.todos:
                index = int(input("\n请输入要删除的任务编号: "))
                todo.delete(index)

        else:
            print("❌ 无效选项")


if __name__ == "__main__":
    main()
