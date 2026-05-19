// 📂 File: src/components/Navbar.jsx

function Navbar() {
  let logoName = "Maaz.Dev";

  return (
    <nav style={styles.navBar}>
      {/* Dynamic Logo */}
      <div style={styles.logo}>{logoName}</div>
      
      {/* Menu Links */}
      <ul style={styles.navLinks}>
        <li style={styles.link}>Home</li>
        <li style={styles.link}>Projects</li>
        <li style={styles.link}>About</li>
        <li style={styles.link}>Contact</li>
      </ul>
    </nav>
  );
}

// Elite Minimalist CSS Setup
const styles = {
  navBar: {
    display: 'flex',
    justifyContent: 'between',
    justifyContent: 'space-between',
    alignItems: 'center',
    background: '#1a1a1a',
    padding: '15px 40px',
    color: '#ffffff',
    boxShadow: '0 2px 10px rgba(0,0,0,0.3)',
  },
  logo: {
    fontSize: '24px',
    fontWeight: 'bold',
    letterSpacing: '1px',
    color: '#4fa9ff', // Professional blue tint
  },
  navLinks: {
    display: 'flex',
    listStyle: 'none',
    gap: '25px',
    margin: 0,
    padding: 0,
  },
  link: {
    fontSize: '16px',
    cursor: 'pointer',
    transition: 'color 0.3s ease',
  }
};

export default Navbar;