import streamlit as st
import feedparser

def show_blogs():
    st.title("AI Education Blogs 📖")
    st.write("Stay updated with the latest AI news and research from top blogs.")   
    rss_feeds = [
        "https://machinelearningmastery.com/blog/feed/",
        # "https://deepmind.com/blog/feed/basic/",
        # "https://openai.com/blog/rss/",
        # "https://www.artificial-intelligence.blog/feed/",
        # "https://www.unite.ai/feed/"
    ]
    
    for url in rss_feeds:
        feed = feedparser.parse(url)
        st.header(f"Source: {feed.feed.title}")
        for entry in feed.entries[:5]:
            st.subheader(entry.title)
            st.write(f"Published on: {entry.published}")
            st.write(entry.summary)
            st.markdown(f"[Read more]({entry.link})")
            st.markdown("---")
