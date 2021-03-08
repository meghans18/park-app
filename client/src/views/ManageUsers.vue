<template>
    <div id="manageUsers" class="container">
        <p>Manage Park app users</p>
        <span v-if="this.users">
            <table class="table table-hover">
                <thead>
                    <tr>
                    <th scope="col">First Name</th>
                    <th scope="col">Last Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">Privilege</th>
                    <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="user in users" :key="user.id">
                        <td>{{ user.first_name }}</td>
                        <td>{{ user.last_name }}</td>
                        <td>{{ user.email }}</td>
                        <td>{{ user.privilege }}</td>
                        <td>
                            <div class="btn-group" role="group">
                            <button type="button" class="btn btn-warning btn-sm" @click="addTowing(user)">Add Towing</button>
                            <button type="button" class="btn btn-danger btn-sm" @click="banUser(user)">Ban User</button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </span>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ManageUsers',
    data() {
        return {
            users: null,
        }
    },
    methods: {
        getUsers() {
            const path = 'http://localhost:5000/users';
            axios.get(path).then((response) => {
                console.log(response)
                this.users = response.data.users
            }).catch((error) => {
                console.error(error);
            });
        },
        banUser(userData) {
            const path = `http://localhost:5000/users/${userData.id}`;
            axios.delete(path).then((response) => {
                console.log(response)
                this.getUsers();
            }).catch((error) => {
                console.error(error);
            }); 
        },
        addTowing(userData) {
            const path = `http://localhost:5000/users/${userData.id}`;
            axios.put(path).then((response) => {
                console.log(response)
                this.getUsers();
            }).catch((error) => {
                console.error(error);
            }); 
        }
    },
    created: function() {
        this.getUsers()
    },
}
</script>

<style scoped>
p {
  color: #0a814c;
  font-size: 2em;
}
</style>