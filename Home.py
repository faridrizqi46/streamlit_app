import streamlit as st

def run():
    st.set_page_config(
        page_title="Home",
        page_icon="👋",
    )

    st.write("# Welcome to My Web Portfolio 👋")

    st.sidebar.success("Select a page above.")

    st.markdown(
        """
        This website was created to test the machine learning models that I have created. \n 
        Select the page on the left to try out the machine learning model.  
        
        Don't forget to visit my LinkedIn [Here](https://www.linkedin.com/in/farid-rizqi-1256111b8/)  
        
        Also visit my other portfolios [Here](https://linktr.ee/faridrizqi12)
        
    """
    )

if __name__ == "__main__":
    run()
