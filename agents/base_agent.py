from abc import ABC, abstractmethod
import logging

class BaseAgent(ABC):
    def __init__(self, name: str, model_config: dict):
        self.name = name
        self.config = model_config
        self.logger = logging.getLogger(name)
        logging.basicConfig(level=logging.INFO)

    @abstractmethod
    async def run(self, task_input: str):
        """所有 Agent 必须实现异步运行方法"""
        pass