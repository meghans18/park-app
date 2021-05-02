<template>
    <div id="manage-spots" class="container">
        <p style="color: #0a814c; font-size: 2em;">All Current Reservations</p>
        <b-input-group >
            <b-form-input v-model="city" placeholder="Filter by city: "></b-form-input>
            <b-input-group-append>
            </b-input-group-append>
        </b-input-group>

        <br>

            <div v-if="city == null || city == ''">
            <table class="table table-hover">
                <thead>
                    <tr>
                    <th scope="col">Car</th>
                    <th scope="col">Spot Address</th>
                    <th scope="col">Spot Number</th>
                    <th scope="col">Spot Price</th>
                    <th scope="col">Date</th>
                    <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="reservation in reservations" :key="reservation.reservationNum">
                    <td>{{reservation.car}}</td>
                    <td>{{reservation.addressNum}} {{reservation.street}}, {{reservation.city}}, {{reservation.state}} {{reservation.zipcode}}</td>
                    <td>{{reservation.spotNumber}}</td>
                    <td>${{reservation.price}}/per day</td>
                    <td>{{reservation.date}}</td>
                    <td>
                        <button type="button" class="btn btn-danger btn-sm" @click="tow(reservation)">
                            Towed?
                        </button>
                    </td>
                    </tr>
                </tbody>
            </table>
            </div>

             <div v-else>
            <table class="table table-hover">
                <thead>
                    <tr>
                    <th scope="col">Car</th>
                    <th scope="col">Spot Address</th>
                    <th scope="col">Spot Number</th>
                    <th scope="col">Spot Price</th>
                    <th scope="col">Date</th>
                    <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="reservation in filteredRes" :key="reservation.reservationNum">
                    <td>{{reservation.car}}</td>
                    <td>{{reservation.addressNum}} {{reservation.street}}, {{reservation.city}}, {{reservation.state}} {{reservation.zipcode}}</td>
                    <td>{{reservation.spotNumber}}</td>
                    <td>${{reservation.price}}/per day</td>
                    <td>{{reservation.date}}</td>
                    <td>
                        <button type="button" class="btn btn-danger btn-sm" @click="tow(reservation)">
                            Towed?
                        </button>
                    </td>
                    </tr>
                </tbody>
            </table>
            </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'ManageSpots',
    data() {
        return {
            reservations: [],
            city: null,
            status: 'not_towed'
        }
    },
    computed: {
        filteredRes() {
            return this.reservations.filter((res) => { 
            return res.city == this.city
            });
        }
    },
    methods: {
        getReservations() {
            const path = `http://localhost:5000/reservations`
            axios.get(path).then((response) => {
                this.reservations = response.data.reservations
            })
        },
        tow(res) {
            console.log(res)
            const payload = {
                'reservationID': res.reservationNum
            }
            const path = 'http://localhost:5000/reservations'
            axios.post(path, payload).then((response) => {
                if (response.data.status == 'success') this.getReservations()
            })
        }
    },
    mounted: function() {
        this.getReservations();
    }
}
</script>