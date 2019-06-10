<template>
  <div class="home">
    <img alt="GNU Health Federation" src="../assets/logo.png">
    <Welcome msg="Welcome to the GNU Health Federation Portal"/>
    <footer>
        GNU Health (c) GNU Solidario GPL v3+
    </footer>
  </div>
</template>

<script>
// @ is an alias to /src
import Welcome from '@/components/Welcome.vue'

export default {
  name: 'home',
  components: {
    Welcome
  }
}
</script>
