import NavBar from './components/NavBar.js';
import styles from './App.module.css';
import  Container  from 'react-bootstrap/Container';



function App() {
  return (
    <div className={styles.App}>
      <NavBar />
      <Container>
        <h1> League News</h1>
        <h1>Sign in</h1>
      </Container>
    </div>
  );
}

export default App;
