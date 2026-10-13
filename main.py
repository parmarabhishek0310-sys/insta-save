import streamlit as st
import instaloader
import os

# Streamlit पेज की सेटिंग
st.title("Insta Save - Instagram Downloader")
st.write("किसी भी इंस्टाग्राम पोस्ट या रील का लिंक यहाँ डालें और डाउनलोड करें।")

# यूजर से इनपुट लेने के लिए टेक्स्ट बॉक्स
post_url = st.text_input("Enter Instagram Post / Reel URL:")

if st.button("Download"):
    if post_url:
        try:
            L = instaloader.Instaloader()
            
            # URL से शॉर्टकोड साफ़ तरीके से निकालना (क्वेरी पैरामीटर हटाकर)
            clean_url = post_url.split("?")[0]
            shortcode = clean_url.split("/")[-2]
            
            with st.spinner("Downloading... Please wait..."):
                post = instaloader.Post.from_shortcode(L.context, shortcode)
                target_dir = "instagram_media"
                L.download_post(post, target=target_dir)
            
            st.success(f"Successfully downloaded from: {post.owner_username}")
            
            # डाउनलोड फोल्डर में से .mp4 फाइल ढूँढना
            video_file = None
            for root, dirs, files in os.walk(target_dir):
                for file in files:
                    if file.endswith(".mp4"):
                        video_file = os.path.join(root, file)
                        break
            
            # अगर वीडियो मिल जाए, तो यूजर को डाउनलोड बटन दिखाएं
            if video_file and os.path.exists(video_file):
                with open(video_file, "rb") as f:
                    st.download_button(
                        label="📥 Click here to save video on your device",
                        data=f,
                        file_name=os.path.basename(video_file),
                        mime="video/mp4"
                    )
            else:
                st.warning("Post downloaded on server, but video format file was not found.")
                
        except Exception as e:
            st.error(f"Error occurred: {e}")
    else:
        st.warning("Please enter a valid URL first!")
        
