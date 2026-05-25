// 📂 File: src/components/Footer.jsx

function Footer() {
  // JavaScript dynamic year nikalne ke liye
  let currentYear = new Date().getFullYear(); 

  return (
    <footer style={styles.footerContainer}>
      <p style={styles.text}>
        &copy; {currentYear} | Designed with ❤️ by <strong>Maaz Usmani</strong>
      </p>
      <div style={styles.socials}>
        <span style={styles.icon}>GitHub</span>
        <span style={styles.icon}>LinkedIn</span>
      </div>
    </footer>
  );
}

const styles = {
  footerContainer: {
    background: '#111111',
    color: '#888888',
    textAlign: 'center',
    padding: '20px',
    position: 'fixed',
    left: '0',
    bottom: '0',
    width: '100%',
    display: 'flex',
    flexDirection: 'column',
    gap: '10px',
    borderTop: '1px solid #222222',
  },
  text: {
    margin: 0,
    fontSize: '14px',
  },
  socials: {
    display: 'flex',
    justifyContent: 'center',
    gap: '20px',
    fontSize: '13px',
  },
  icon: {
    cursor: 'pointer',
    color: '#4fa9ff',
  }
};

export default Footer;