<template>
    <div class="main-page">
      <div class="main-field">
        <form enctype="application/json" class="wrapper">
          <div class="main-description" id="11">
            <h1>Terra</h1>
            <h3>Create your account</h3>
          </div>
          <div class="inputs">
            <input type="text" name="username" id="username" placeholder="Username">
            <span class="error" id="email-error">Введите действительный адрес</span>
            <input type="text" name="email" id="email" placeholder="Email">
            <span class="error" id="pass-error">password must be at leat 7 symbols</span>
            <input type="password" name="password" id="password" placeholder="Password">
            <!-- <input type="password" name="password-repeat" id="password-repeat" placeholder="Repeat password" v-model="password"> -->
            <button type="submit">
              SignUp
            </button>
            <p>or</p>
            <RouterLink to='/login' name="register" id="register">
              <p>Go to login</p>
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
    animation: gradient 15s ease infinite;
    height: 100vh;
}
.wrapper {
    justify-content: space-between;
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
    padding: 20px;
    background-color: var(--bg-color);
    width: 400px;
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
    width: 100%;
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
.error {
    display: none;
    font-size: 0.8rem;
    margin-left: 0px;
    width: 100%;
    color: gray;
    animation: 0.5s show ease;
    padding-bottom: 3px;
}
@keyframes show {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
  
<script setup>
import axios, { formToJSON } from 'axios';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();

onMounted(() => {
    const login_field = document.getElementById('username')
    const email_field = document.getElementById('email')
    const password_field = document.getElementById('password')

    login_field.addEventListener("input", () => {
        if (login_field.value.length <= 1) {
            login_field.style.border = '1px solid rgba(255, 0, 0, 0.5)';
        } else {
            login_field.style.border = 'none';
        }
    })
    email_field.addEventListener("input", () => {
        if (!email_field.value.includes('@')) {
            email_field.style.border = '1px solid rgba(255, 0, 0, 0.5)';
            document.getElementById('email-error').style.display = 'block';
        } else {
            email_field.style.border = 'none';
            document.getElementById('email-error').style.display = 'none';
        }
    })
    password_field.addEventListener("input", () => {
        if (password_field.value.length <= 6) {
            password_field.style.border = '1px solid rgba(255, 0, 0, 0.5)';
            document.getElementById('pass-error').style.display = 'block';
        } else {
            password_field.style.border = 'none';
            document.getElementById('pass-error').style.display = 'none';
        }
    })
    const form = document.querySelector("form");
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const user = new FormData(form);
        await axios.post(
            '/auth/register',
            formToJSON(user)
        )
        .then(() => {
            router.push("/login");
        }, (error) => {
            console.log(error);
        });
    })
})
</script>