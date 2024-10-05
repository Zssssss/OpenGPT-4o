import gradio as gr
from gradio.components.multimodal_textbox import MultimodalData
from gradio.components.chatbot import FileDataDict, Message, MessageDict, TupleFormat
from typing import AsyncGenerator, Callable, Literal, Union, cast
from gradio.events import Dependency, on
from gradio.utils import SyncToAsyncIterator, async_iteration, async_lambda
from gradio.routes import Request
from gradio.helpers import special_args
import anyio
from gradio.components import (
    Button,
    Chatbot,
    Component,
    Markdown,
    MultimodalTextbox,
    State,
    Textbox,
    get_component_instance,
)




class MyMultimodalData(MultimodalData):
    other_params: str | MultimodalData | None






class MyChatInterface(gr.ChatInterface):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    async def _delete_prev_fn(
        self,
        message: str | MultimodalData | None,
        history: list[MessageDict] | TupleFormat,
    ) -> tuple[
        list[MessageDict] | TupleFormat,
        str | MultimodalData,
        list[MessageDict] | TupleFormat,
    ]:
        # temp = MyMultimodalData()
        extra = 1 if self.type == "messages" else 0
        if self.multimodal and isinstance(message, MultimodalData):
            remove_input = (
                len(message.files) + 1
                if message.text is not None
                else len(message.files)
            ) + extra
            # temp.__dict__.update(message.__dict__)
            message.__class__ = MyMultimodalData
            message.other_params = history[-remove_input:][0][-1]
            # message = temp
            history = history[:-remove_input]
        else:
            message.__class__ = MyMultimodalData
            message.other_params = history[-(1 + extra):][0][-1]
            history = history[: -(1 + extra)]
        return history, message or ""  # type: ignore