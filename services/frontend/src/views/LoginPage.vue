<template>
  <div class="main-page">
    <div class="main-field">
      <form class="wrapper">
        <div class="main-description">
          <h1>Terra</h1>
          <h3>Соцсеть</h3>
        </div>
        <div class="inputs">
          <input type="text" name="username" id="username" placeholder="Username">
          <input type="password" name="password" id="password" placeholder="Password">
          <button type="submit">
            Login
          </button>
          <p>or</p>
          <RouterLink to='/signup' name="register" id="register">
            <p>SignUp</p>
          </RouterLink>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.main-page {
	background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
	background-size: 400% 400%;
	animation: gradient 10s ease infinite;
	height: 100vh;
}
.wrapper {
  justify-content: space-between;
  width: 100%;
}
@keyframes gradient {
	0% {
		background-position: 0% 50%;
	}
	50% {
		background-position: 100% 50%;
	}
	100% {
		background-position: 0% 50%;
	}
}
.main-field {
  margin: 10px;
  padding: 1rem;
  background-color: var(--bg-color);
  max-width: 400px;
  border-radius: 15px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 13px 27px -5px, rgba(0, 0, 0, 0.3) 0px 8px 16px -8px;
}
.main-description {
    width: 100%;
    text-align: center; 
}
input {
  margin-bottom: 10px;
  font-size: 16px;
}
button {
  margin-top: 10px;
  margin-bottom: 10px;
}
.inputs {
  margin-top: 40px;
}
.inputs a {
  text-align: center;
  text-decoration: none;
  color: gray;
}
a:active,
a:hover,
a::after {
  text-decoration: none;
  background-color: none;
  color: none;
  -webkit-tap-highlight-color: transparent;
}
p {
  margin-bottom: 10px;
  text-align: center;
}
</style>

<script setup>
import router from '@/router';
import { useAuthStore } from '@/store/auth';
import { onMounted } from 'vue';


const authStore = useAuthStore();


onMounted(async () => {
  if (authStore.user) {
    router.push('/');
  };
  const form = document.querySelector("form");
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const userData = new FormData(form);
    authStore.login(userData);
  });
})
</script>@/store/auth