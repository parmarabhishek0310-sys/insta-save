import instaloader

# Instaloader की एक इंस्टेंस बनाएं
L = instaloader.Instaloader()

def download_instagram_post(post_url):
    try:
        # URL से शॉर्टकोड (Shortcode) निकालें
        shortcode = post_url.split("/")[-2]
        
        # पोस्ट की जानकारी प्राप्त करें
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        
        # पोस्ट (फोटो या वीडियो) डाउनलोड करें
        print(f"Downloading post from: {post.owner_username}")
        L.download_post(post, target=f"{post.owner_username}_post")
        print("Download complete!")
        
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    # जिस इंस्टाग्राम पोस्ट/रील्स को डाउनलोड करना है, उसका URL यहाँ डालें
    url = input("Enter Instagram Post / Reel URL: ")
    download_instagram_post(url)
    
