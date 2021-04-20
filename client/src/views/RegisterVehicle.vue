<template>
    <div id="register-vehicle" class="container">
        <b-alert v-model="showError" variant="danger" dismissible>
            Failed to register vehicle!
        </b-alert>
        <div class="text-center">
            <p style="color: #0a814c; font-size: 2em;">Register Vehicles</p>
        </div>

        <button type="button" class="btn btn-success btn-md" v-b-modal.vehicle-modal>Add a New Vehicle</button>

        <br>
        <br>

        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Vehicle</th>
              <th scope="col">Plate Number</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="vehicle in vehicles" :key="vehicle.id">
                <td>{{vehicle.year}} {{vehicle.make}} {{vehicle.model}} {{vehicle.color}}</td>
                <td>{{vehicle.plateNumber}}</td>
            </tr>
          </tbody>
        </table>


        <b-modal ref="addVehicleModal"
                id="vehicle-modal"
                title="Add a New Vehicle"
                centered
                hide-footer>
            <b-form @submit.prevent="onSubmit" @reset="onReset" class="w-100">
                <b-form-group id="form-year-group"
                            label="Year:"
                            label-for="form-year-input">
                    <b-form-input id="form-year-input"
                                type="number"
                                v-model="form.year"
                                required
                                placeholder="Enter year:">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-make-group"
                                label="Make:"
                                label-for="form-make-input">
                    <b-form-input id="form-make-input"
                                    type="text"
                                    v-model="form.make"
                                    required
                                    placeholder="Enter make:">
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-model-group"
                                label="Model:"
                                label-for="form-model-input">
                    <b-form-input id="form-model-input"
                                    type="text"
                                    v-model="form.model"
                                    required
                                    placeholder="Enter model:">
                    </b-form-input>
                </b-form-group>

                <b-form-group id="form-color-group" label="Color:" label-for="form-color-input">
                    <b-form-select
                        id="form-color-input"
                        v-model="form.color"
                        :options="colors"
                        required
                    ></b-form-select>
                </b-form-group>

                <b-form-group id="form-plateNumber-group"
                                label="Plate Number:"
                                label-for="form-plateNumber-input">
                    <b-form-input id="form-plateNumber-input"
                                    type="text"
                                    v-model="form.plateNumber"
                                    required
                                    placeholder="Enter plate number:">
                    </b-form-input>
                </b-form-group>
                <b-button type="submit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "RegisterVehicle",
    data() {
        return {
            form: {
                year: '',
                make: '',
                model: '',
                color: '',
                plateNumber: '',
            },
            vehicles: [],
            showError: false,
            colors: ['Brown', 'Black', 'Gray', 'White', 'Orange', 'Blue', 'Red', 'Yellow', 'Green', 'Purple'],
        }
    },
    methods: {
        deleteCar(carData) {
            const path = `http://localhost:5000/vehicles/${carData.id}`;
            axios.delete(path).then(() => {
                this.getUserRegisteredVehicles();
            }).catch((error) => {
                console.error(error);
            }); 
        },
        getUserRegisteredVehicles() {
            let userEmail = this.$store.getters.getEmail
            const path = `http://localhost:5000/vehicles/${userEmail}`
            axios.get(path).then((response) => {
                this.vehicles = response.data.vehicles
            })
        },
        addVehicle(payload) {
            console.log(payload)
            const path = 'http://localhost:5000/vehicles';
            axios.post(path, payload).then((response) => {
                if (response.data.status == 'failed') { 
                    this.onReset();
                    this.showError = true;
                } else {
                    this.onReset()
                    this.$bvModal.hide('vehicle-modal')
                    this.getUserRegisteredVehicles();
                }
            }).catch((error) => {
                console.log(error);
                this.$router.push("/")
            });
        },
        onSubmit() {
            const payload = {
                email: this.$store.getters.getEmail,
                year: this.form.year,
                make: this.form.make,
                model: this.form.model,
                color: this.form.color,
                plateNumber: this.form.plateNumber
            };
            this.addVehicle(payload);
        },
        onReset() {
            this.form.year = ''
            this.form.make = ''
            this.form.model = ''
            this.form.color = ''
            this.form.plateNumber = ''
        }
    },
    created: function() {
        this.getUserRegisteredVehicles();
    }
}
</script>