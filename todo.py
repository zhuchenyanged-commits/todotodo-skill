#!/usr/bin/env python3
"""
待办事项清单 Skill v1.0
简单的任务管理工具
"""

class TodoList:
    """待办事项列表"""

    def __init__(self):
        self.todos = []

    def add(self, task):
        """添加任务"""
        self.todos.append({"task": task, "done": False})
        print(f"✅ 已添加任务: {task}")

    def list(self):
        """列出所有任务"""
        if not self.todos:
            print("📝 暂无任务")
            return

        print("\n📋 待办事项清单:")
        print("-" * 50)
        for i, todo in enumerate(self.todos, 1):
            status = "✓" if todo["done"] else " "
            print(f"{i}. [{status}] {todo['task']}")
        print("-" * 50)

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
    print("待办事项清单 v1.0".center(50))
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
                todo.add(task)

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
