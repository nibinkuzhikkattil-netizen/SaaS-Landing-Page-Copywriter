import streamlit as st

from saas_landing_page_copywriter.crew import SaaSCopywriterCrew


def main():
    st.set_page_config(
        page_title="SaaS Landing Page Copywriter",
        page_icon="🚀",
        layout="wide"
    )

    st.title("🚀 SaaS Landing Page Copywriter")
    st.markdown(
        "Generate high-converting SaaS landing page copy using CrewAI agents."
    )

    # Sidebar
    st.sidebar.header("Product Details")

    product_name = st.sidebar.text_input(
        "Product Name",
        placeholder="Example: FlowCRM"
    )

    target_audience = st.sidebar.text_input(
        "Target Audience",
        placeholder="Freelancers, startups, agencies..."
    )

    product_description = st.sidebar.text_area(
        "Describe Your SaaS Product",
        placeholder=(
            "Explain what your SaaS product does, "
            "its features, benefits, and problems it solves."
        ),
        height=250
    )

    generate_button = st.sidebar.button("Generate Landing Page Copy")

    if generate_button:

        if not product_description:
            st.sidebar.error("Please enter your SaaS product description.")
            return

        inputs = {
            "product_description": f"""
            Product Name: {product_name}

            Target Audience: {target_audience}

            Product Description:
            {product_description}
            """
        }

        with st.spinner("Generating landing page copy..."):

            result = SaaSCopywriterCrew().crew().kickoff(inputs=inputs)

        st.success("Landing page copy generated successfully!")

        # Task Outputs
        positioning_output = result.tasks_output[0].raw
        copy_output = result.tasks_output[1].raw
        cta_output = result.tasks_output[2].raw

        # Tabs
        tab1, tab2, tab3 = st.tabs(
            [
                "🎯 Positioning Strategy",
                "📝 Landing Page Copy",
                "🔥 CTA Variants"
            ]
        )

        with tab1:
            st.subheader("Positioning Strategy")
            st.text_area(
                "Strategy",
                positioning_output,
                height=500
            )

            st.download_button(
                "Download Strategy",
                positioning_output,
                file_name="positioning_strategy.md"
            )

        with tab2:
            st.subheader("Landing Page Copy")

            st.text_area(
                "Copy",
                copy_output,
                height=700
            )

            st.download_button(
                "Download Landing Page Copy",
                copy_output,
                file_name="landing_page_copy.md"
            )

        with tab3:
            st.subheader("CTA Variants")

            st.text_area(
                "CTA Suggestions",
                cta_output,
                height=500
            )

            st.download_button(
                "Download CTA Variants",
                cta_output,
                file_name="cta_variants.md"
            )


if __name__ == "__main__":
    main()