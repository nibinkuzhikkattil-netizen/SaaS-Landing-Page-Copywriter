from saas_landing_page_copywriter.crew import SaaSCopywriterCrew


def run():
    product_description = input("Describe your SaaS product: ")

    inputs = {
        "product_description": product_description
    }

    SaaSCopywriterCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()