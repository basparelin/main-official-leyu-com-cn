from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    title: str
    content: str
    keyword: str
    source_url: str
    created_at: Optional[datetime] = None
    tags: Optional[List[str]] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.tags is None:
            self.tags = []

    def format_brief(self) -> str:
        return f"[{self.keyword}] {self.title}"

    def format_full(self) -> str:
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"标题：{self.title}\n"
            f"关键词：{self.keyword}\n"
            f"来源：{self.source_url}\n"
            f"标签：{tag_str}\n"
            f"创建时间：{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"内容：{self.content}"
        )


def format_notes_as_text(notes: List[KeywordNote], separator: str = "\n---\n") -> str:
    return separator.join(note.format_full() for note in notes)


def format_notes_as_html(notes: List[KeywordNote]) -> str:
    html_parts = ["<ul>"]
    for note in notes:
        tag_items = "".join(f"<li>{tag}</li>" for tag in note.tags)
        html_parts.append(
            f"<li>"
            f"<strong>{note.title}</strong> "
            f"（关键词：{note.keyword}）<br>"
            f"来源：<a href='{note.source_url}'>{note.source_url}</a><br>"
            f"标签：<ul>{tag_items}</ul>"
            f"<p>{note.content}</p>"
            f"</li>"
        )
    html_parts.append("</ul>")
    return "\n".join(html_parts)


def filter_notes_by_keyword(notes: List[KeywordNote], keyword: str) -> List[KeywordNote]:
    return [note for note in notes if note.keyword == keyword]


def main():
    sample_notes = [
        KeywordNote(
            title="乐鱼体育平台简介",
            content="乐鱼体育是一家致力于体育赛事服务的在线平台，提供多种体育项目的投注与资讯服务。",
            keyword="乐鱼体育",
            source_url="https://main-official-leyu.com.cn",
            tags=["体育", "投注", "平台"],
        ),
        KeywordNote(
            title="乐鱼体育最新活动",
            content="乐鱼体育近期推出会员专属活动，涵盖足球、篮球等热门赛事，欢迎广大用户参与体验。",
            keyword="乐鱼体育",
            source_url="https://main-official-leyu.com.cn/events",
            tags=["活动", "足球", "篮球"],
        ),
        KeywordNote(
            title="乐鱼体育注册指南",
            content="新用户注册乐鱼体育账号流程简单，只需填写基本资料并完成手机验证即可开始使用。",
            keyword="乐鱼体育",
            source_url="https://main-official-leyu.com.cn/register",
            tags=["注册", "指南"],
        ),
        KeywordNote(
            title="其他体育平台对比",
            content="本文对比了多家体育服务平台，乐鱼体育在用户界面和赛事覆盖上表现突出。",
            keyword="乐鱼体育",
            source_url="https://main-official-leyu.com.cn/compare",
            tags=["对比", "评测"],
        ),
    ]

    print("=== 纯文本格式输出 ===")
    print(format_notes_as_text(sample_notes))

    print("\n=== HTML 格式输出 ===")
    print(format_notes_as_html(sample_notes))

    print("\n=== 按关键词过滤（乐鱼体育） ===")
    filtered = filter_notes_by_keyword(sample_notes, "乐鱼体育")
    for note in filtered:
        print(note.format_brief())


if __name__ == "__main__":
    main()