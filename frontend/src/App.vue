<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import HelloWorld from './components/HelloWorld.vue'

const message = ref('Loading from API...')
const apiStatus = ref('connecting')

onMounted(async () => {
  try {
    // In dev, Vite proxies might be used, but in production Nginx will proxy /api to backend
    // Since we are running in docker, we can just fetch from /api
    const response = await axios.get('/api/hello')
    message.value = response.data.message
    apiStatus.value = 'success'
  } catch (error) {
    console.error('API Error:', error)
    message.value = 'Failed to load from API'
    apiStatus.value = 'error'
  }
})
</script>

<template>
  <div class="app-container">
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo vite" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
    
    <h1>Vue 3 + FastAPI</h1>

    <div class="card">
      <h2>Backend Response:</h2>
      <p :class="['api-response', apiStatus]">{{ message }}</p>
    </div>

    <HelloWorld msg="Vite + Vue API Demo" />
  </div>
</template>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  text-align: center;
  background-color: #242424;
  color: rgba(255, 255, 255, 0.87);
}

.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

.card {
  margin: 2rem 0;
  padding: 2em;
  background-color: #1a1a1a;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border: 1px solid #333;
}

.api-response {
  font-size: 1.5rem;
  font-weight: bold;
  margin-top: 1rem;
}

.success {
  color: #42b883; /* Vue Green */
}

.error {
  color: #ff4c4c;
}

.connecting {
  color: #f39c12;
}
</style>
