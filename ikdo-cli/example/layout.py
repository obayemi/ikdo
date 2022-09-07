import itertools
from dataclasses import dataclass

from rich.panel import Panel
from rich.table import Table
from textual.app import App
from textual.reactive import Reactive
from textual.views import DockView
from textual.widget import Widget
from textual.widgets import Placeholder


@dataclass
class TodoItem:
    title: str
    done: bool = False


todoItemsContent = [
    TodoItem(title="hey"),
    TodoItem(title="thing item", done=True),
    TodoItem(title="olala"),
]


class TodoItemsList(Widget):
    items = Reactive([])
    current_item = Reactive(TodoItem("hey"))

    def status_display(self, item: TodoItem):
        return "[*]" if item.done else "[ ]"

    def render(self) -> Table:
        grid = Table.grid(expand=True)
        grid.add_column("Status", width=4)
        grid.add_column("Title", ratio=1)
        for item in self.items:
            if item.title == self.current_item.title:
                grid.add_row(
                    self.status_display(item),
                    f"[bold]{item.title}",
                    style="on blue",
                )
            else:
                grid.add_row("" + self.status_display(item), item.title)
        return grid


class SimpleApp(App):
    async def on_mount(self) -> None:
        self.todoList = TodoItemsList("listpane")
        self.todoList.items = todoItemsContent
        self.selectionCycle = itertools.cycle(self.todoList.items)
        await self.view.dock(self.todoList, edge="left")

    async def on_load(self, event):
        await self.bind("j", "select_next()")
        await self.bind("k", "select_prev()")
        await self.bind("l", "select_option()")
        await self.bind("q", "quit")

    async def action_select_next(self) -> None:
        print("next todo handler called")
        self.todoList.current_item = next(self.selectionCycle)

    async def action_select_prev(self) -> None:
        print("prev todo handler called")
        for i in range(len(self.todoList.items) - 1):
            self.todoList.current_item = next(self.selectionCycle)
    
    async def action_select_option(self) -> None:
        print("select option handler called")
        # remove current selected item
        self.todoList.current_item.done = not self.todoList.current_item.done
        self.todoList.current_item = next(self.selectionCycle)


    async def action_exit(self) -> None:
        exit()


SimpleApp.run(log="textual.log")
