from pydantic import BaseModel
from typing import List


class Topic(BaseModel):
    topic_name: str
    subtopics: List[str]


class Section(BaseModel):
    section_title: str
    section_description: str
    topics: List[Topic]


class LearningPath(BaseModel):
    roadmap_title: str
    sections: List[Section]
    learning_goal_summary: str