import concurrent.futures

from agent_data_mesh import main as data_mesh_main
from agent_documentation import main as documentation_main
from agent_refactor import main as refactor_main
from agent_requirements import main as requirements_main
from agent_review import main as reviews_main
from agent_security import main as security_main
from agent_tests import main as tests_main
from agent_whatsnext import main as whats_next_main

if __name__ == '__main__':
    # Using ThreadPoolExecutor to run functions in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(documentation_main),
            executor.submit(data_mesh_main),
            executor.submit(refactor_main),
            executor.submit(tests_main),
            executor.submit(requirements_main),
            executor.submit(reviews_main),
            executor.submit(security_main),
            executor.submit(whats_next_main),
        ]

        # Waiting for all futures to complete
        for future in concurrent.futures.as_completed(futures):
            future.result()  # This will also re-raise any exceptions caught during function execution
