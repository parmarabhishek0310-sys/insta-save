import streamlit as st
import instaloader

# Streamlit पेज की सेटिंग
st.title("Insta Save - Instagram Downloader")
st.write("किसी भी इंस्टाग्राम पोस्ट या रील का लिंक यहाँ डालें और डाउनलोड करें।")

# यूजर से इनपुट लेने के लिए टेक्स्ट बॉक्स
post_url = st.text_input("Enter Instagram Post / Reel URL:")

if st.button("Download"):
    if post_url:
        try:
            L = instaloader.Instaloader()
            # URL से शॉर्टकोड निकालें
            shortcode = post_url.split("/")[-2]
            
            with st.spinner("Downloading... Please wait..."):
                post = instaloader.Post.from_shortcode(L.context, shortcode)
                L.download_post(post, target="instagram_media")
            
            st.success(f"Successfully downloaded from: {post.owner_username}")
            
        except Exception as e:
            st.error(f"Error occurred: {e}")
    else:
        st.warning("Please enter a valid URL first!")
