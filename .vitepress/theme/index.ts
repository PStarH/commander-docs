import DefaultTheme from 'vitepress/theme'
import Layout from './Layout.vue'
import Home from './components/Home.vue'
import './style.css'

export default {
  extends: DefaultTheme,
  Layout,
  enhanceApp({ app }) {
    app.component('Home', Home)
  },
}
