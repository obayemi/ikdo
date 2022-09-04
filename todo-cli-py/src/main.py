from textual.app import App
from textual.widgets import Placeholder
from textual.widget import Widget
from rich.panel import Panel

todoItemsContent = [
        "hey",
        "thing item",
        "olala"
        ]

class TodoItem(Widget):
    def render(self) -> str:
        return "Hello world"

class SimpleApp(App):
    async def on_mount(self) -> None:
        items = (TodoItem() for itemContent in todoItemsContent)
        await self.view.dock(*items, size=1, edge="top")


SimpleApp.run(log="textual.log")
