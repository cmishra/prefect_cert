from prefect.filesystems import GitHub
from prefect.deployments import Deployment

from lab103 import lab103_do_analysis

github_block = GitHub.load("prefect-cert")

dep = Deployment.build_from_flow(
    flow=lab103_do_analysis,
    name="lab103_do_analysis",
    tags=["demo2"],
    # storage=github_block,
)

if __name__ == '__main__':
    dep.apply()