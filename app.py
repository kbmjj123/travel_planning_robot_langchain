import gradio as gr
from agents import exec_agent

with gr.Blocks() as travel_planner:
    gr.Markdown("基于LangChain的旅游规划助手")
    with gr.Row(equal_height=True) as chat_interface:
        chat_interface.elem_classes = ["full-height"]
        # 左边日志输出
        with gr.Column(scale=1):
            debug_info = gr.Textbox(
                label = "调试信息",
                lines = 30,
                interactive=False,
                elem_id = "debug-info"
            )
        with gr.Column(scale=3):
            chat_history = gr.Chatbot(
                label="Chat History",
                show_label=False,
                type="messages",
                elem_id="chatbot"
            )
            user_input = gr.Textbox(
                label="User Input",
                placeholder="请输入你的问题...",
                lines=3,
                max_lines=5,
                show_label=False,
                elem_id="user-input"
            )
            send = gr.Button("发送")

            send.click(
                exec_agent,
                inputs=[
                    user_input,
                    debug_info,
                    chat_history
                ],
                outputs=[
                    chat_history,
                    debug_info
                ]
            )
    travel_planner.launch(debug=True)