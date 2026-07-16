import streamlit as st

# ==============================================================================
# 1. PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Junior Heri Farid | Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. PREMIUM GLASSMORPHISM & ANIMATED GRADIENT STYLING (CSS)
# ==============================================================================
st.markdown(
    """
    <!-- Font Awesome CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts (Poppins) -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        /* Base Reset and Fonts */
        * {
            font-family: 'Poppins', sans-serif;
        }
        
        /* Smooth Scrolling */
        html {
            scroll-behavior: smooth;
        }
        
        /* Premium Animated Blue Gradient Background */
        .stApp {
            background: linear-gradient(-45deg, #0f172a, #1e3a8a, #0369a1, #0f172a);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            color: #f1f5f9;
        }
        
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Hide Streamlit Header, Footer, and Main Menu */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display:none;}
        
        /* Remove default Streamlit top padding to make hero flush */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 3rem !important;
            max-width: 1200px !important;
        }

        /* Custom Navigation Bar */
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(15, 23, 42, 0.45);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 1rem 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
            animation: fadeInDown 0.8s ease;
        }
        
        .navbar-brand {
            font-weight: 700;
            font-size: 1.25rem;
            color: #38bdf8;
            letter-spacing: 0.5px;
        }
        
        .navbar-links {
            display: flex;
            gap: 1.5rem;
        }
        
        .navbar-links a {
            color: #cbd5e1;
            text-decoration: none;
            font-weight: 500;
            font-size: 0.9rem;
            transition: color 0.3s ease;
        }
        
        .navbar-links a:hover {
            color: #38bdf8;
        }

        /* Glassmorphism Cards */
        .glass-card {
            background: rgba(15, 23, 42, 0.45);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.25);
            transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
            margin-bottom: 1.5rem;
            animation: fadeInUp 1s ease;
        }
        
        .glass-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px 0 rgba(56, 189, 248, 0.15);
            border-color: rgba(56, 189, 248, 0.3);
        }

        /* Hero Banner */
        .hero {
            text-align: center;
            padding: 4rem 2rem;
            margin-bottom: 2rem;
        }
        
        .hero h1 {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(to right, #ffffff, #38bdf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            animation: scaleIn 0.8s ease;
        }
        
        .hero p {
            font-size: 1.25rem;
            color: #94a3b8;
            margin-bottom: 1.5rem;
            animation: fadeInUp 1s ease;
        }
        
        .hero-btn {
            display: inline-block;
            background: linear-gradient(135deg, #2563eb, #38bdf8);
            color: white;
            padding: 0.75rem 2rem;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .hero-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(56, 189, 248, 0.6);
            color: white;
        }

        /* Profile Photo Container */
        .profile-pic-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 1.5rem;
        }
        
        .profile-pic {
            border-radius: 50%;
            border: 4px solid rgba(56, 189, 248, 0.4);
            box-shadow: 0 10px 25px rgba(0,0,0,0.4);
            transition: transform 0.5s ease;
            object-fit: cover;
        }
        
        .profile-pic:hover {
            transform: rotate(3deg) scale(1.02);
            border-color: #38bdf8;
        }

        /* Section Titles */
        .section-title {
            font-size: 1.75rem;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 1.5rem;
            border-left: 5px solid #2563eb;
            padding-left: 0.75rem;
        }

        /* Hobbies and Badges */
        .hobby-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
            margin-top: 1rem;
        }
        
        .hobby-badge {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 0.5rem 1rem;
            border-radius: 30px;
            font-weight: 500;
            font-size: 0.85rem;
            transition: background 0.3s, transform 0.3s;
        }
        
        .hobby-badge:hover {
            background: rgba(56, 189, 248, 0.2);
            transform: scale(1.05);
            border-color: #38bdf8;
        }

        /* Social Links Grid */
        .social-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
        }
        
        .social-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 1rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            text-decoration: none;
            color: #cbd5e1;
            transition: all 0.3s ease;
        }
        
        .social-card:hover {
            background: rgba(56, 189, 248, 0.1);
            border-color: rgba(56, 189, 248, 0.3);
            transform: translateY(-3px);
            color: #38bdf8;
        }
        
        .social-icon {
            font-size: 1.5rem;
            color: #38bdf8;
        }

        /* Useful Links Styling */
        .useful-links-list {
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }
        
        .useful-link-item {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 0.75rem 1.25rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            text-decoration: none;
            color: #f1f5f9;
            font-weight: 500;
            transition: all 0.3s;
        }
        
        .useful-link-item:hover {
            background: rgba(37, 99, 235, 0.15);
            border-color: rgba(37, 99, 235, 0.4);
            transform: translateX(5px);
            color: #38bdf8;
        }

        /* Embed elements formatting */
        .video-wrapper {
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }

        /* Animations declarations */
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes scaleIn {
            from { opacity: 0; transform: scale(0.9); }
            to { opacity: 1; transform: scale(1); }
        }
        
        /* Responsive tweaks */
        @media (max-width: 768px) {
            .navbar {
                flex-direction: column;
                gap: 1rem;
                padding: 1rem;
            }
            .hero h1 {
                font-size: 2rem;
            }
            .social-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================================================================
# 3. NAVIGATION BAR
# ==============================================================================
st.markdown(
    """
    <div class="navbar">
        <div class="navbar-brand">
            <i class="fa-solid fa-graduation-cap"></i> JHF Portfolio
        </div>
        <div class="navbar-links">
            <a href="#home"><i class="fa-solid fa-house"></i> Home</a>
            <a href="#about-me"><i class="fa-solid fa-user"></i> About</a>
            <a href="#gallery"><i class="fa-solid fa-images"></i> Gallery</a>
            <a href="#education-video"><i class="fa-solid fa-play"></i> Video</a>
            <a href="#social-media"><i class="fa-solid fa-share-nodes"></i> Links</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Anchor tag for navigation
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

# ==============================================================================
# 4. HERO SECTION
# ==============================================================================
st.markdown(
    """
    <div class="hero">
        <h1>Hello, I'm Junior Heri Farid</h1>
        <p>Bachelor Student | Future Professional</p>
        <a href="#about-me" class="hero-btn">Explore My Profile <i class="fa-solid fa-arrow-down"></i></a>
    </div>
    """,
    unsafe_allow_html=True
)

# Layout Setup: 2 Columns for main details
col1, col2 = st.columns([1, 2], gap="large")

# ==============================================================================
# 5. LEFT COLUMN: PROFILE CARD, IDOL & HOBBIES
# ==============================================================================
with col1:
    # Student Bio Card
    st.markdown(
        """
        <div class="glass-card" style="text-align: center;">
            <div class="profile-pic-container">
                <img class="profile-pic" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=350&h=350" alt="Student Profile" width="180px" height="180px">
            </div>
            <h3 style="margin-bottom: 0.25rem;">Junior Heri Farid</h3>
            <p style="color: #38bdf8; font-size: 0.9rem; margin-bottom: 1rem; font-weight: 500;">MZA/BAC/2528041</p>
            <hr style="border-color: rgba(255,255,255,0.1); margin: 1rem 0;">
            <div style="text-align: left; font-size: 0.9rem; line-height: 1.8;">
                <p><i class="fa-solid fa-university" style="color: #38bdf8; width: 25px;"></i> College Student</p>
                <p><i class="fa-solid fa-earth-africa" style="color: #38bdf8; width: 25px;"></i> Tanzania</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Hobbies Badge Card
    st.markdown(
        """
        <div class="glass-card">
            <h4 style="margin-bottom: 0.5rem; font-weight: 600;"><i class="fa-solid fa-heart" style="color: #e11d48; margin-right: 0.5rem;"></i> Hobbies</h4>
            <div class="hobby-grid">
                <div class="hobby-badge">🎮 Gaming</div>
                <div class="hobby-badge">📚 Reading Novels</div>
                <div class="hobby-badge">🤝 Making Friends</div>
                <div class="hobby-badge">⚽ Football</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==============================================================================
# 6. RIGHT COLUMN: ABOUT ME, GALLERY, VIDEO, AND LINKS
# ==============================================================================
with col2:
    # About Me Card with Idol Accent
    st.markdown('<div id="about-me"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card">
            <div class="section-title">About Me</div>
            <p style="line-height: 1.7; color: #cbd5e1; margin-bottom: 1.5rem;">
                Hello everyone! My name is <strong>Junior Heri Farid</strong>. I enjoy playing games and reading novels in my free time. 
                My idol is <strong>Cristiano Ronaldo</strong> because his hard work, discipline, and determination inspire me to always do my best. 
                I love college because it helps me learn new skills, gain knowledge, and connect with people from different backgrounds. 
                I enjoy making new friends and growing both academically and personally. My goal is to keep learning, work hard, and achieve success in my future career. Thank you!
            </p>
            <div style="background: rgba(56, 189, 248, 0.08); border-left: 4px solid #38bdf8; padding: 1rem; border-radius: 0 12px 12px 0;">
                <h5 style="margin: 0 0 0.25rem 0; color: #38bdf8; font-weight: 600;"><i class="fa-solid fa-crown"></i> My Idol: Cristiano Ronaldo</h5>
                <p style="margin: 0; font-size: 0.85rem; color: #94a3b8; font-style: italic;">
                    "His hard work, discipline and determination inspire me every day."
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Gallery Card
    st.markdown('<div id="gallery"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card">
            <div class="section-title">Gallery</div>
            <p style="font-size: 0.9rem; color: #cbd5e1; margin-bottom: 1.5rem;">Memories, campus moments, and hobbies from my college life.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    # Using columns for responsive gallery styling
    img_col1, img_col2 = st.columns(2)
    with img_col1:
        st.markdown(
            """
            <div style="border-radius:15px; overflow:hidden; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 1rem;">
                <img src="https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&q=80&w=600" alt="College Campus Life" style="width: 100%; height: 180px; object-fit: cover; display:block;">
            </div>
            """,
            unsafe_allow_html=True
        )
    with img_col2:
        st.markdown(
            """
            <div style="border-radius:15px; overflow:hidden; border: 1px solid rgba(255,255,255,0.1); margin-bottom: 1rem;">
                <img src="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&q=80&w=600" alt="Tech & Study Sessions" style="width: 100%; height: 180px; object-fit: cover; display:block;">
            </div>
            """,
            unsafe_allow_html=True
        )

    # Video Card
    st.markdown('<div id="education-video"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card">
            <div class="section-title">Education Video</div>
            <p style="font-size: 0.9rem; color: #cbd5e1; margin-bottom: 1.5rem;">Explore university culture and the power of academic development.</p>
            <div class="video-wrapper">
        """,
        unsafe_allow_html=True
    )
    # 16:9 YouTube video embed
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    st.markdown("</div></div>", unsafe_allow_html=True)

    # Links Card (Social Media & Useful Links Combined)
    st.markdown('<div id="social-media"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card">
            <div class="section-title">Connect & Learn</div>
            <p style="font-size: 0.9rem; color: #cbd5e1; margin-bottom: 1.5rem;">Stay updated with my socials and explore key academic platforms.</p>
        """,
        unsafe_allow_html=True
    )
    
    # Grid: 2 Inner columns for social vs links
    link_col1, link_col2 = st.columns(2, gap="medium")
    with link_col1:
        st.markdown("<h5 style='font-weight: 600; margin-bottom: 1rem;'>Social Media</h5>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="social-grid">
                <a href="https://instagram.com/its_h.a.n.z.o" target="_blank" class="social-card">
                    <i class="fa-brands fa-instagram social-icon"></i>
                    <div>
                        <div style="font-size: 0.75rem; color: #94a3b8;">Instagram</div>
                        <div style="font-weight: 600; font-size: 0.85rem;">@its_h.a.n.z.o</div>
                    </div>
                </a>
                <a href="https://instagram.com/7xh78" target="_blank" class="social-card">
                    <i class="fa-brands fa-instagram social-icon"></i>
                    <div>
                        <div style="font-size: 0.75rem; color: #94a3b8;">Instagram</div>
                        <div style="font-weight: 600; font-size: 0.85rem;">@7xh78</div>
                    </div>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    with link_col2:
        st.markdown("<h5 style='font-weight: 600; margin-bottom: 1rem;'>Useful Links</h5>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="useful-links-list">
                <a href="https://ifm.ac.tz" target="_blank" class="useful-link-item">
                    <span>IFM Portal</span>
                    <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.8rem;"></i>
                </a>
                <a href="https://google.com" target="_blank" class="useful-link-item">
                    <span>Google Search</span>
                    <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.8rem;"></i>
                </a>
                <a href="https://youtube.com" target="_blank" class="useful-link-item">
                    <span>YouTube Library</span>
                    <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.8rem;"></i>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# 7. FOOTER
# ==============================================================================
st.markdown(
    """
    <div style="text-align: center; margin-top: 4rem; padding: 2rem 0; border-top: 1px solid rgba(255,255,255,0.1); color: #64748b; font-size: 0.9rem;">
        <p style="margin: 0;">Created with ❤️ by <strong>Junior Heri Farid</strong> &copy; 2026</p>
        <p style="margin: 0.25rem 0 0 0; font-size: 0.8rem; color: #475569;">Streamlit Glassmorphism Design Framework</p>
    </div>
    """,
    unsafe_allow_html=True
)
