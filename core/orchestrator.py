import asyncio
from agents.architect import ArchitectAgent
from agents.coder import CoderAgent


class NexusOrchestrator:
    def __init__(self):
        self.status = "Idle"
        # 模拟初始化不同的 Agent
        self.architect = ArchitectAgent(name="Arch-01", config={"model": "gemini-1.5-pro"})
        self.coder = CoderAgent(name="Code-01", config={"model": "claude-3.5-sonnet"})

    async def execute_workflow(self, project_path: str):
        print(f"🚀 [Orchestrator] Starting workflow for: {project_path}")

        # 第一阶段：架构分析
        analysis = await self.architect.run(f"Scan {project_path}")
        print(f"✅ [Analysis Complete] Findings: {analysis[:50]}...")

        # 第二阶段：根据分析结果进行代码重构
        if "critical" in analysis:
            refactor_results = await self.coder.run(analysis)
            print(f"✨ [Refactor Complete] {refactor_results}")

        self.status = "Finished"