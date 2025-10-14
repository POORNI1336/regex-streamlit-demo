import re
import streamlit as st

# --- Configuration and Title ---
st.set_page_config(layout="wide")
st.title("Regular Expression Tester 🧪")
st.markdown("An interactive tool to test Python's `re` module functionalities.")

# --- Input Area ---
col1, col2 = st.columns(2)

with col1:
    text = st.text_area("✍️ Enter Text to Search (Source String):", 
                        "The email addresses are user@example.com and support@project.net. Revision date: 2023-10-14.", 
                        height=200)

with col2:
    pattern = st.text_input("🔍 Enter Regex Pattern:", r"\b\w+@\w+\.\w+\b")
    
    # Flags selection
    flags = st.multiselect(
        '⚙️ Select Regex Flags',
        ['re.IGNORECASE (i)', 're.MULTILINE (m)', 're.DOTALL (s)', 're.VERBOSE (x)'],
        default=[]
    )
    
    # Map selected flags to re. constants
    re_flags = 0
    if 're.IGNORECASE (i)' in flags:
        re_flags |= re.IGNORECASE
    if 're.MULTILINE (m)' in flags:
        re_flags |= re.MULTILINE
    if 're.DOTALL (s)' in flags:
        re_flags |= re.DOTALL
    if 're.VERBOSE (x)' in flags:
        re_flags |= re.VERBOSE

# --- Regex Operation Selection ---
operation = st.selectbox(
    "Choose Regex Operation:",
    ['findall (Get all matches)', 'search (Find first match)', 'match (Match from start)', 'sub (Substitution)']
)

# --- Substitution Input (only visible for 'sub') ---
replacement = None
if 'sub' in operation:
    replacement = st.text_input("📝 Enter Replacement String:", r"[EMAIL REDACTED]")

st.markdown("---")

# --- Run Button and Logic ---
if st.button("🚀 Run Regex Test", type="primary"):
    try:
        # --- Handle re.sub operation ---
        if 'sub' in operation and replacement is not None:
            st.header("✅ Substitution Result (`re.sub`)")
            
            # Perform substitution
            substituted_text, count = re.subn(pattern, replacement, text, flags=re_flags)
            
            st.success(f"Successfully replaced **{count}** occurrence(s).")
            st.code(substituted_text, language='text')

        # --- Handle Find/Search/Match operations ---
        else:
            st.header("✨ Match Results")
            
            if 'findall' in operation:
                matches = re.findall(pattern, text, flags=re_flags)
                st.info(f"Total **{len(matches)}** match(es) found using `re.findall()`.")
                st.code(matches)
            
            elif 'search' in operation:
                match = re.search(pattern, text, flags=re_flags)
                if match:
                    st.success("First match found using `re.search()`.")
                    st.json({
                        "Match String": match.group(0),
                        "Start Index": match.start(),
                        "End Index": match.end(),
                    })
                    matches = [match.group(0)] # For visualization
                else:
                    st.warning("No match found using `re.search()`.")
                    matches = []
            
            elif 'match' in operation:
                match = re.match(pattern, text, flags=re_flags)
                if match:
                    st.success("Match found from the start of the string using `re.match()`.")
                    st.json({
                        "Match String": match.group(0),
                        "Start Index": match.start(),
                        "End Index": match.end(),
                    })
                    matches = [match.group(0)] # For visualization
                else:
                    st.warning("No match found from the start of the string using `re.match()`.")
                    matches = []

            # --- Visual Highlighting (Only for Find/Search/Match) ---
            if matches:
                st.subheader("Visual Highlight")
                
                # Use a simpler findall for highlighting for better robustness
                highlight_matches = list(re.finditer(pattern, text, flags=re_flags))
                
                highlighted_text = ""
                last_end = 0
                
                for match in highlight_matches:
                    start, end = match.span()
                    # Add non-matching text
                    highlighted_text += text[last_end:start]
                    # Add highlighted match
                    highlighted_text += f"<mark style='background-color:#ADD8E6; padding: 2px 4px; border-radius: 3px;'>{text[start:end]}</mark>"
                    last_end = end
                
                # Add remaining text
                highlighted_text += text[last_end:]

                st.markdown(highlighted_text, unsafe_allow_html=True)
                
    except re.error as e:
        st.error(f"❌ Invalid Regex Pattern: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
