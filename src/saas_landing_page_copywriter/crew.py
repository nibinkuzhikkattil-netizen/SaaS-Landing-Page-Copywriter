from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew

from saas_landing_page_copywriter.tools.hero_copy_length_checker import HeroCopyLengthChecker


@CrewBase
class SaaSCopywriterCrew:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def positioning_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config["positioning_strategist"],
            verbose=True
        )

    @agent
    def copy_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["copy_writer"],
            verbose=True,
            tools=[HeroCopyLengthChecker()]
        )

    @agent
    def cta_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config["cta_optimizer"],
            verbose=True
        )

    @task
    def positioning_task(self) -> Task:
        return Task(
            config=self.tasks_config["positioning_task"]
        )

    @task
    def copywriting_task(self) -> Task:
        return Task(
            config=self.tasks_config["copywriting_task"],
            output_file="output/landing_page_copy.md"
        )

    @task
    def cta_task(self) -> Task:
        return Task(
            config=self.tasks_config["cta_task"]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )